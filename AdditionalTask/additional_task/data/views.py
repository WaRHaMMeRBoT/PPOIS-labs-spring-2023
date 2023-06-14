from django.shortcuts import render
from .models import Medicine
from .forms import Form


def main_page(request):
    items = Medicine.objects.all()
    return render(request, "index.html", {"items": items})


def filtering(request):
    form = Form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            date_of_birth = form.cleaned_data["date_of_birth"]
            date_of_visit = form.cleaned_data["name_of_doctor"]
            name_of_doctor = form.cleaned_data["name_of_doctor"]
            conclusion = form.cleaned_data["conclusion"]
            items = Medicine.objects.filter(name=name,
                                            address=address,
                                            date_of_birth=date_of_birth,
                                            date_of_visit=date_of_visit,
                                            name_of_doctor=name_of_doctor,
                                            conclusion=conclusion)
            return render(request, "index.html", {"items": items})
    return render(request, "filter.html", {"form": Form})


def creating(request):
    form = Form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            date_of_birth = form.cleaned_data["date_of_birth"]
            date_of_visit = form.cleaned_data["name_of_doctor"]
            name_of_doctor = form.cleaned_data["name_of_doctor"]
            conclusion = form.cleaned_data["conclusion"]
            item = Medicine.objects.create(name=name,
                                           address=address,
                                           date_of_birth=date_of_birth,
                                           date_of_visit=date_of_visit,
                                           name_of_doctor=name_of_doctor,
                                           conclusion=conclusion)
            item.save()
            items = Medicine.objects.all()
            return render(request, "index.html", {"items": items})
    return render(request, "create.html", {"form": Form})


def deleting(request):
    form = Form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            date_of_birth = form.cleaned_data["date_of_birth"]
            date_of_visit = form.cleaned_data["name_of_doctor"]
            name_of_doctor = form.cleaned_data["name_of_doctor"]
            conclusion = form.cleaned_data["conclusion"]
            items = Medicine.objects.filter(name=name,
                                            address=address,
                                            date_of_birth=date_of_birth,
                                            date_of_visit=date_of_visit,
                                            name_of_doctor=name_of_doctor,
                                            conclusion=conclusion)
            items.delete()
            items = Medicine.objects.all()
            return render(request, "index.html", {"items": items})
    return render(request, "delete.html", {"form": Form})
