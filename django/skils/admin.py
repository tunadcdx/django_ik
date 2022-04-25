from django.contrib import admin

from skils.models import Skils
# Register your models here.


class SkilAdmin(admin.ModelAdmin):
    list_display = ("skilName",)

def __str__(self):
        return f"{self.skilName}"
        
admin.site.register(Skils, SkilAdmin)
