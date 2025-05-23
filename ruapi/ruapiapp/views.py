from django.shortcuts import render
from .models import Person
from .utils import load_persons


def index(request):

    log = ""
    if request.method == "POST":
        pa_value = request.POST.get("pa", "")
        load_persons(int(pa_value))
        log = f"{pa_value} users were added"

    persons = Person.objects.all().order_by('-id')

    return render(request, "ruapiapp/index.html", context={"persons": persons, "log": log})
