from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
class Ahang(models.Model):
    # author, description, ahang, publish and update date
    author = models.CharField(max_length=200)
    description = RichTextUploadingField()
    ahang_esm = models.CharField(max_length=500, default=None)
    ahang_file = models.FileField(upload_to='Musics/', null=False, blank=False)
    publishDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("music:detail", args=[str(self.id)])

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = "Music's"
        
