from datetime import date
from django.db import models
from skils.models import Skils
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from workers.models import Workers

# Create your models here.


class userProfil(models.Model):

    profilePicture = models.ImageField(
        upload_to="img_user", verbose_name="Firma Logo/ Görsel",)
    coverLetter = RichTextField()
    autoBiography = RichTextField()
    autoBiographyFile = models.FilePathField()
    birtDate = models.CharField(max_length=50)
    skils = models.ManyToManyField(Skils)
    works = models.ManyToManyField(Workers)
    userField = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

