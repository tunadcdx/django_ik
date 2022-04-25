from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Companys(models.Model):
    comName = models.CharField(
        max_length=50, null=False,  verbose_name="Firma Adı",)
    comEmail = models.EmailField(null=False, verbose_name="Email Adresi",)
    comAddres = models.TextField(verbose_name="Firma Adresi",)
    comWebAdrdes = models.URLField(null=True,verbose_name="Firma Web Adresi",)
    comPicture = models.ImageField(
        upload_to="img_com", verbose_name="Firma Logo/ Görsel",)
    comPhoneNumber = models.BigIntegerField(
        null=False, verbose_name="Telefon Numarası",)
    comAbout = RichTextField(null=False,  verbose_name="Firma Hakkında",)
