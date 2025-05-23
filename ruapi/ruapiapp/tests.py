from django.test import TestCase
from ruapiapp.utils import load_persons


class MyModelTest(TestCase):
    def test_load(self):
        load_persons(10000)
