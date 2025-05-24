from django.test import TestCase
from ruapiapp.utils import load_persons
from unittest.mock import patch, MagicMock
import requests
from django.urls import reverse
from ruapiapp.models import Person


class MyModelTest(TestCase):
    @patch("requests.get")
    def test_load_persons(self, mock_get):
        fake_response = {
            "results": [
                {
                    "name": {"first": "Иван", "last": "Иванов"},
                    "gender": "male",
                    "phone": "+7 999 123-45-67",
                    "email": "ivan@example.com",
                    "location": {
                        "street": {"name": "Ленина, 10"},
                        "city": "Москва",
                        "country": "Россия"
                    },
                    "picture": {"large": "https://example.com/photo.jpg"}
                }
            ]
        }

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = fake_response
        mock_get.return_value = mock_response

        result = load_persons(4000)
        assert result == 1, "fail"


class IndexViewTest(TestCase):
    def test_index_page_loads(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ruapiapp/index.html")


class IndexPaginationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем 15 пользователей для проверки пагинации
        for i in range(30):
            Person.objects.create(name=f"User{i}")

    def test_pagination(self):
        response = self.client.get(reverse("index") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["page_obj"].has_previous())
        self.assertTrue(response.context["page_obj"].has_next())


class IndexPostTest(TestCase):
    def test_invalid_post_request(self):
        response = self.client.post(reverse("index"), {"pa": "abc"})
        self.assertRedirects(response, reverse("index"))  # Должно редиректить обратно
        messages = list(response.wsgi_request._messages)
        self.assertEqual(messages[0].message, "Invalid data. Try again")


class UserDetailTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name="Иван")

    def test_existing_user_detail(self):
        response = self.client.get(reverse("user_detail", args=[self.person.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ruapiapp/person_detail.html")


class RandomUserTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name="Иван")

    def test_random_person(self):
        response = self.client.get(reverse("random"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ruapiapp/person_detail.html")
        self.assertIn("person", response.context)



