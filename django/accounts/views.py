
from distutils.command.upload import upload
from multiprocessing import context
from skils.models import Skils
from .models import userProfil
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from workers.models import Categorys, Workers
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
# Create your views here.

# Login Control


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_view")
    if request.method == "POST":
        email = request.POST["Emailaddress"]
        password = request.POST["Password"]
        if User.objects.filter(email=email) is not None:
            s = User.objects.get(email=email)
            user = authenticate(
                request, username=s.username, password=password)
            if user is not None:
                if user.is_superuser == False and user.is_staff == False:

                    if user.is_active:
                        login(request, user)
                        return redirect("home_view")
                elif user.is_superuser or user.is_staff == True:

                    return render(request, "accounts/login.html", {
                        "error": "Kullanıcı Bu Giriş İçin Yetkili Değildir."})
                else:
                    return render(request, "accounts/login.html", {
                        "error": "Kullanıcı Üyeligi Aktif Değildir."})
            else:
                return render(request, "accounts/login.html", {
                    "error": "Email ya da Şifre Hatalı"
                })
        else:
            return render(request, "accounts/login.html", {
                "error": "Email ya da Şifre Hatalı"
            })
    else:
        return render(request, "accounts/login.html")

# Register Control


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home_view")
    if request.method == "POST":
        username = request.POST["name"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            if User.objects.filter(email=email).exists():
                return render(request, "accounts/register.html", {"error": "Bu Email Adresi Kullanılıyor.",
                                                                  "name": username,
                                                                  "lastname": lastname,
                                                                  "email": email,
                                                                  "password": password,
                                                                  })
            else:
                user = User.objects.create_user(username=username+lastname,
                                                first_name=username, last_name=lastname, email=email, password=password)
                user.save()
                us = userProfil.objects.create(
                    userField=User.objects.get(id=user.id))
                us.save()
                login(request, user)
                return redirect("profile")
        else:
            return render(request, "accounts/register.html", {"error": "Parolalar Eşleşmiyor.", "name": username,
                                                              "lastname": lastname,
                                                              "email": email,
                                                              "password": password, })
    else:
        return render(request, "accounts/register.html")

# Register Control


def logout_request(request):
    logout(request)
    return redirect("home_view")

# Profile


def profile_request(request):
    if request.method == "POST":
        userProfile = userProfil.objects.get(userField_id=request.user.id)
        choices = request.POST.getlist('skils')
        coverLetter = request.POST.get("covtter")
        autoBiography = request.POST.get("autoBiography")

        upload = request.FILES["autoBiographyFile"]
        print("upload" ,upload)
        if userProfile.autoBiographyFile != upload:
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                file_url = fss.url(file)
                userProfile.autoBiographyFile=file_url
                userProfile.save()
            
        birtDate = request.POST.get("birtDate")
        userProfile.coverLetter = coverLetter,
        userProfile.autoBiography = autoBiography,
        userProfile.birtDate = birtDate
        userProfile.save()
        for i in choices:
            userProfile.skils.add(request.user.id, i)
        context = userSkilsCheck(request.user.id)
        return render(request, "accounts/profile.html", context)
    elif request.method == "GET":
        context = userSkilsCheck(request.user.id)
        return render(request, "accounts/profile.html", context)
    else:
        return render(request, "accounts/profile.html")

# Profile Picture


def profilePic_request(request):
    if request.method == 'POST' and request.FILES['profilePicture']:
        upload = request.FILES['profilePicture']
        userProfile = userProfil.objects.get(userField_id=request.user.id)
        if userProfile.profilePicture != upload:
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            userProfile.profilePicture = file_url
            userProfile.save()
            context = userSkilsCheck(request.user.id)
            return render(request, "accounts/profile.html", context)
        else:
            redirect('profile')
    else:
        context = userSkilsCheck(request.user.id)
        return render(request, "accounts/profile.html",  context)

# Profile Skils


def userSkilsCheck(userid):
    # Kullanıcın Yetkinleri ve tüm yetkinlikler alınarak bir listede birleştirilir
    userProfile = userProfil.objects.get(
        userField_id=userid).skils.all()
    g = []
    skilAll = Skils.objects.difference(userProfile)
    for s2 in userProfile:
        g.append({"id": s2.id, "skilName": s2.skilName, "active": True})
    for s in skilAll:
        g.append({"id": s.id, "skilName": s.skilName, "active": False})
    context = {
        "getUser": userProfil.objects.get(userField=userid),
        "skils": g}
    return context


def addMyWorks_request(request):
    userProfile = userProfil.objects.get(userField_id=request.user.id)
    worker = Workers.objects.get(id=request.POST["workData"])
    userProfile.works.add(worker)
    context = {
        "cats": Categorys.objects.all(),
        "works": userProfile.works.all()
    }
    return render(request, 'works\my_works.html', context)


def myWorks_request(request):
    userProfile = userProfil.objects.get(userField_id=request.user.id)
    context = {
        "cats": Categorys.objects.all(),
        "works": userProfile.works.all()
    }
    return render(request, 'works\my_works.html', context)


def securty_request(request):
    # if request.method == 'POST':
    #     form = PasswordChangeForm(request.user, request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)
    #         messages.success(request, _(
    #             'Your password was successfully updated!'))
    #         return redirect('accounts:securty')
    #     else:
    #         messages.error(request, _('Please correct the error below.'))
    # else:
    #     form = PasswordChangeForm(request.user)
    return render(request, 'accounts/securty.html',)
