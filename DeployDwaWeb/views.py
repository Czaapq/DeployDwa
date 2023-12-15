from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bibik
from .forms import BibikForm
from django.contrib.auth.models import User


def wszystkie_bibiki(request):
    wszystkkie = Bibik.objects.all()
    return render(request, 'bibiki.html', {'bibiki': wszystkkie})


def nowy_bibik(request):
    form = BibikForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_bibiki)

    return render(request, 'bibik_form.html', {'form': form})


def edytuj_bibika(request, id):
    bibik = get_object_or_404(Bibik, pk=id)
    form = BibikForm(request.POST or None,
                     request.FILES or None, instance=bibik)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_bibiki)

    return render(request, 'bibik_form.html', {'form': form})


def usun_bibika(request, id):
    bibik = get_object_or_404(Bibik, pk=id)

    if request.method == "POST":
        bibik.delete()
        return redirect(wszystkie_bibiki)

    return render(request, 'potwierdz.html', {'bibik': bibik})
