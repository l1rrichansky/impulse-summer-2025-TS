from django.shortcuts import render

from django.http import HttpResponse

import requests


def index(request):
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)  # Вывод информации о случайном пользователе
    else:
        print(f"Ошибка: {response.status_code}")
        data = "404"
    return render(request, "ruapiapp/index.html", context={"data": data})
