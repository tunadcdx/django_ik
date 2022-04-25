from django.shortcuts import render
from skils.models import Skils
from workers.models import Workers, Categorys

# Create your views here.


def home_view(request):
    context = {
        "cats": Categorys.objects.all(),
        "works": Workers.objects.filter(isActive=True),
    }
    return render(request, 'home.html', context)
