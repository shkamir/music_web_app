from django.contrib import admin

# Register your models here.
from .models import Ahang


class AhangManager(admin.ModelAdmin):
    list_display = ('author','ahang_esm',)
    list_filter = ('publishDate',)
    search_fields = ('author','ahang_esm',)
    class Meta:
        model = Ahang
    #TODO: show these in template 
admin.site.register(Ahang, AhangManager)