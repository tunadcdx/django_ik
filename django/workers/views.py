from django.shortcuts import render, HttpResponse
from accounts.models import userProfil
from workers.models import Categorys, Workers
# Create your views here.


def workers_detail(request, slug):
    try:
        work = Workers.objects.get(slug=slug)
        userProfile = userProfil.objects.get(works=work)
    except:
        userProfile = ""
    context = {
        "work": work,
        "userProfile": userProfile}
    return render(request, "works/work_detail.html", context)


def workers_update(request, model, exception):

    if not isinstance(exception):
        return None
    else:
        s1 = Workers.objects.get(model.id)
        s1 = model
        s1.save()
        return HttpResponse('<p>workers_update</p>')


def worksByCategorys(request, slug):

    f = []
    for s in Workers.objects.filter(isActive=True):
        print(s)
        for d in Workers.objects.get(id=s.id).skil.all():
            f.append({"workerid": s.id, "skilId": d.id, "skilName": d.skilName})

    context = {
        "works": Categorys.objects.get(slug=slug).workers_set.filter(isActive=True),
        "cats": Categorys.objects.all(),
        "selected_category": slug,
        "skilsByworker": f
    }
    return render(request, "home.html", context)