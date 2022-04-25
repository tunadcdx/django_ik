from datetime import date, datetime
from distutils.text_file import TextFile
from django.utils.text import slugify
from typing_extensions import Self
from unittest.util import _MAX_LENGTH
from django.db import models
from skils.models import Skils
from django.forms import CharField, DateTimeField, NumberInput, SlugField
from ckeditor.fields import RichTextField

# Create your models here.


class Categorys(models.Model):
    catName = models.CharField(max_length=50, verbose_name="Kategori Adı")
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, editable=False)
    isActive = models.BooleanField(default=True, verbose_name="Aktif Mi?")

    def __str__(self):
        return self.catName

    # SlugContent
    def save(self, *args, **kwargs):
        self.slug = slugify(self.catName)
        super().save(*args, **kwargs)


class Workers(models.Model):
    CHOICES = [
        ("Adana", "Adana"),
        ("Adıyaman", "Adıyaman"),
        ("Afyon", "Afyon"),
        ("Ağrı", "Ağrı"),
        ("Amasya", "Amasya"),
        ("Ankara", "Ankara"),
        ("Antalya", "Antalya"),
        ("Artvin", "Artvin"),
        ("Aydın", "Aydın"),
        ("Balıkesir", "Balıkesir"),
        ("Bilecik", "Bilecik"),
        ("Bingöl", "Bingöl"),
        ("Bitlis", "Bitlis"),
        ("Bolu", "Bolu"),
        ("Burdur", "Burdur"),
        ("Bursa", "Bursa"),
        ("Çanakkale", "Çanakkale"),
        ("Çankırı", "Çankırı"),
        ("Çorum", "Çorum"),
        ("Denizli", "Denizli"),
        ("Diyarbakır", "Diyarbakır"),
        ("Edirne", "Edirne"),
        ("Elazığ", "Elazığ"),
        ("Erzincan", "Erzincan"),
        ("Erzurum", "Erzurum"),
        ("Eskişehir", "Eskişehir"),
        ("Gaziantep", "Gaziantep"),
        ("Giresun", "Giresun"),
        ("Gümüşhane", "Gümüşhane"),
        ("Hakkari", "Hakkari"),
        ("Hatay", "Hatay"),
        ("Isparta", "Isparta"),
        ("Mersin", "Mersin"),
        ("İstanbul", "İstanbul"),
        ("İzmir", "İzmir"),
        ("Kars", "Kars"),
        ("Kastamonu", "Kastamonu"),
        ("Kayseri", "Kayseri"),
        ("Kırklareli", "Kırklareli"),
        ("Kırşehir", "Kırşehir"),
        ("Kocaeli", "Kocaeli"),
        ("Konya", "Konya"),
        ("Kütahya", "Kütahya"),
        ("Malatya", "Malatya"),
        ("Manisa", "Manisa"),
        ("Kahramanmaraş", "Kahramanmaraş"),
        ("Mardin", "Mardin"),
        ("Muğla", "Muğla"),
        ("Muş", "Muş"),
        ("Nevşehir", "Nevşehir"),
        ("Niğde", "Niğde"),
        ("Ordu", "Ordu"),
        ("Rize", "Rize"),
        ("Sakarya", "Sakarya"),
        ("Samsun", "Samsun"),
        ("Siirt", "Siirt"),
        ("Sinop", "Sinop"),
        ("Sivas", "Sivas"),
        ("Tekirdağ", "Tekirdağ"),
        ("Tokat", "Tokat"),
        ("Trabzon", "Trabzon"),
        ("Tunceli", "Tunceli"),
        ("Şanlıurfa", "Şanlıurfa"),
        ("Uşak", "Uşak"),
        ("Van", "Van"),
        ("Yozgat", "Yozgat"),
        ("Zonguldak", "Zonguldak"),
        ("Aksaray", "Aksaray"),
        ("Bayburt", "Bayburt"),
        ("Karaman", "Karaman"),
        ("Kırıkkale", "Kırıkkale"),
        ("Batman", "Batman"),
        ("Şırnak", "Şırnak"),
        ("Bartın", "Bartın"),
        ("Ardahan", "Ardahan"),
        ("Iğdır", "Iğdır"),
        ("Yalova", "Yalova"),
        ("Karabük", "Karabük"),
        ("Kilis", "Kilis"),
        ("Osmaniye", "Osmaniye"),
        ("Düzce", "Düzce"),
    ]
    title = models.CharField(max_length=50, verbose_name='İlan Başlık')
    desc = RichTextField(verbose_name='Açıklama')
    startDate = models.DateTimeField(verbose_name='İlan Tarihi')
    endDate = models.DateTimeField(verbose_name='İlan Bitiş Süresi')
    picture = models.ImageField(
        upload_to="img_ad", verbose_name="Logo/ Görsel",)
    slug = models.SlugField(null=False, blank=True,
                            unique=True, db_index=True, editable=False)
    isActive = models.BooleanField(default=True, verbose_name='İlan Aktif mi?')
    location = models.CharField(
        max_length=120, choices=CHOICES, verbose_name='İş Lokasyonu')
    # category = models.ForeignKey(Categorys,on_delete=models.CASCADE, verbose_name='Branş')
    categorys = models.ManyToManyField(Categorys, verbose_name='Branşlar')
    skil = models.ManyToManyField(Skils, verbose_name='Yetkinlikler')

    def __str__(self):
        return f"{self.title}"

    # SlugContent
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
