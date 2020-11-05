from django.contrib import admin

# Register your models here.
from .models import Ahang, CommentDb


class AhangManager(admin.ModelAdmin):
    list_display = ('author','ahang_esm',"isAgreed",)
    list_filter = ('publishDate',"isAgreed",)
    list_editable = ("isAgreed",)
    search_fields = ('author','ahang_esm',)
    class Meta:
        model = Ahang

admin.site.register(Ahang, AhangManager)