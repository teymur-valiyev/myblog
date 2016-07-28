from django.contrib import admin
from .models import About

class aboutModel(admin.ModelAdmin):
    list_display = ['title','timestamp']
    list_display_links = ['title','timestamp']
    class Meta:
        model = About

admin.site.register(About,aboutModel)