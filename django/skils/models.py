from django.db import models

# Create your models here.

class Skils(models.Model):
    skilName = models.CharField(
        verbose_name="Yetenekler / Yetkinlikler", max_length=20)


def __str__(self):
    return self.skilName
