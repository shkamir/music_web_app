from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_file
class Ahang(models.Model):
    # author, description, ahang, publish and update date
    author = models.CharField(max_length=200, blank=False, null=False, unique=False)
    description = RichTextUploadingField()
    ahang_esm = models.CharField(max_length=500, default=None, unique=False)
    ahang_file = models.FileField(upload_to='Musics/', validators=[validate_file])
    publishDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    # user is able to upload music without logging in but music has to be checked by admin
    isAgreed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("music:detail", args=[str(self.id)])

    def __str__(self):
        return "{author}-{ahang_esm}-{id}".format(author=self.author, ahang_esm=self.ahang_esm,id=self.id)
    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = "Music's"
    
class CommentDb(models.Model):
    # text, is read, date
    user_name= models.CharField(max_length=200, default="nUmberX")
    comment = models.TextField()
    email = models.EmailField(default="example@example.com")
    isRead = models.BooleanField(default=False)
    def __str__(self):
        return "{username}-{email}".format(username=self.user_name, email=self.email)
    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact's"
