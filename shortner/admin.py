from django.contrib import admin
from .models import Url, AnalyticData

class UrlAdmin(admin.ModelAdmin):
    pass


admin.site.register(Url, UrlAdmin)