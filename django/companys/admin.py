from django.contrib import admin

from companys.models import Companys

# Register your models here.


class CompanysAdmin(admin.ModelAdmin):

    list_display = ('comPicture', 'comName', 'comEmail',
                    'comPhoneNumber',)
    list_filter = ('comName', 'comEmail',)
    list_display_links = ('comName',)


admin.site.register(Companys, CompanysAdmin)
