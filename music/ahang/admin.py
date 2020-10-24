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
  
class CommentsManager(admin.ModelAdmin):
    list_display = ('comment','isRead',)
    list_filter = ('isRead',)
    search_fields = ('comment',)
    list_editable = ("isRead",)
    class Meta:
        model = CommentDb
  
admin.site.register(Ahang, AhangManager)
admin.site.register(CommentDb, CommentsManager)