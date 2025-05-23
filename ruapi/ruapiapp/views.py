from django.shortcuts import render, get_object_or_404
from .models import Person
from .utils import load_persons
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):

    if request.method == "POST":
        pa_value = request.POST.get("pa", "")
        load_persons(int(pa_value))
        messages.success(request, f"{pa_value} users were added")
        return redirect(request.path)

    persons = Person.objects.all().order_by('-id')
    paginator = Paginator(persons, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    total = Person.objects.count()

    return render(request, "ruapiapp/index.html", context={"persons": persons, "page_obj": page_obj, "total": total})


def user_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    return render(request, "ruapiapp/person_detail.html", {"person": person})


def random(request):
    random_person = Person.objects.order_by('?').first()
    return render(request, "ruapiapp/person_detail.html", {"person": random_person})