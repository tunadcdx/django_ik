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

    if not isinstance(exception, SomeExceptionType):
        return None
    else:
        s1 = Workers.objects.get(model.id)
        s1 = model
        s1.save()
        return HttpResponse('<p>workers_update</p>')


def worksByCategorys(request, slug):

    context = {
        "works": Categorys.objects.get(slug=slug).workers_set.filter(isActive=True),
        # "works": Workers.objects.filter(isActive=True, category__slug=slug),
        "cats": Categorys.objects.all(),
        "selected_category": slug
    }
    works = Categorys.objects.get(slug=slug)
    return render(request, "home.html", context)


# def test(request):
#     categories = Workers.objects.annotate(Count('category_id'))
#     # return HttpResponse(Categorys.objects.annotate(nblog=Count('category_id')))

#     print(
#     categories.aggregate(models.Count('id'))['id__count']
#         )
