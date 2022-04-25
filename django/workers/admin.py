from django.contrib import admin
from .models import Workers, Categorys
from django.utils.safestring import mark_safe
# Register your models here.


class WorkerAdmin(admin.ModelAdmin):

    list_display = ('title', 'Kategoriler', 'Yetkinlikler',
                    'startDate', 'isActive')
    list_display_links = ('title', 'startDate')
    list_filter = ('title', 'startDate')
    search_fields = ('title', 'desc', 'startDate')
    list_editable = ('isActive',)

    def Kategoriler(self, obj):
        html = "<ul>"
        for category in obj.categorys.all():
            html += "<li>" + category.catName + "</li>"
        html += "</ul>"
        return mark_safe(html)

    def Yetkinlikler(self, obj):
        html = "<ul>"
        for s in obj.skil.all():
            html += "<li>" + s.skilName + "</li>"
        html += "</ul>"
        return mark_safe(html)


class CategorysAdmin(admin.ModelAdmin):
    list_display = ('catName', 'isActive')
    list_filter = ('catName',)
    list_editable = ('isActive',)


# Register Site
admin.site.register(Categorys, CategorysAdmin)
admin.site.register(Workers, WorkerAdmin)
