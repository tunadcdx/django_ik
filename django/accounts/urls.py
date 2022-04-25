from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile_request, name="profile"),
    path("securty", views.securty_request, name="securty"),
    path("myWorks", views.myWorks_request, name="myWorks"),
    path("register", views.register_request, name="register"),
    path("addMyWorks", views.addMyWorks_request, name="addMyWorks"),
    path("profilePic", views.profilePic_request, name="profilePic")
    
]
