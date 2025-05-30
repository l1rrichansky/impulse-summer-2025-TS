import requests
from .models import Person


def load_persons(n):
    if n not in range(1, 5000):
        print("1 <= n <= 5000")
        return 0
    url = f"https://randomuser.me/api/?results={n}"
    response = requests.get(url)
    if response.status_code == 200:
        for data in response.json()["results"]:
            person = Person(
                name=data["name"]["first"],
                surname=data["name"]["last"],
                gender=data["gender"],
                number=data["phone"],
                email_address=data["email"],
                address=f'{data["location"]["street"]["name"]}, {data["location"]["city"]}, {data["location"]["country"]}',
                photo_url=data["picture"]["large"]
            )
            person.save()
        return 1
    else:
        print(f"Ошибка: {response.status_code}")
        return 2
