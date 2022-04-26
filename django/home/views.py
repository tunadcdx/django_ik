from msilib.schema import PublishComponent
from django.shortcuts import render
from skils.models import Skils
from workers.models import Workers, Categorys

# Create your views here.
 
def home_view(request):

    f = []
    for s in Workers.objects.filter(isActive=True):
        print(s)
        for d in Workers.objects.get(id=s.id).skil.all():
            f.append({"workerid": s.id, "skilId": d.id, "skilName": d.skilName})

    context = {
        "cats": Categorys.objects.all(),
        "works": Workers.objects.filter(isActive=True),
        "skilsByworker":f
    }
    return render(request, 'home.html', context)
