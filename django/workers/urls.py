from . import views
from django.urls import path

urlpatterns = [
    path('update/', views.workers_update),
    path('categorys/<slug:slug>', views.worksByCategorys, name="worksByCategorys"),
    path('detail/<slug:slug>', views.workers_detail, name='workers_detail'),
]
