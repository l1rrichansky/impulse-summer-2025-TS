from django.shortcuts import render, get_object_or_404
from .models import Person
from .utils import load_persons
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):

    if request.method == "POST":
        try:
            pa_value = int(request.POST.get("pa", ""))
        except Exception as e:
            messages.error(request, f"Invalid data. Try again")
            return redirect(request.path)
        if pa_value>5000 or pa_value<0 or pa_value%1!=0:
            messages.error(request, f"Invalid data. Try again")
            return redirect(request.path)
        res = load_persons(pa_value)
        if res == 2:
            messages.error(request, f"Service not responding. Try again later")
            return redirect(request.path)
        messages.success(request, f"{pa_value} users were added")
        return redirect(request.path)

    persons = Person.objects.all().order_by('-id')
    paginator = Paginator(persons, 12)
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