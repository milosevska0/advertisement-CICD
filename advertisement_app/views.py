from django.shortcuts import render, redirect
from .models import Category, Advertisement
from .forms import AdvertisementForm


# Create your views here.
def index(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'index.html', {'advertisements': advertisements})


def details(request, adv_id):
    advertisement = Advertisement.objects.get(id=adv_id)
    return render(request, 'details.html', {'advertisement': advertisement})


def add_advertisement(request):
    if request.method == 'POST':
        advertisement_form = AdvertisementForm(request.POST, request.FILES)
        if advertisement_form.is_valid():
            advertisement_form.save()
            return redirect("index")
    else:
        advertisement_form = AdvertisementForm()
    return render(request, 'add-advertisement.html', {'form': advertisement_form})


