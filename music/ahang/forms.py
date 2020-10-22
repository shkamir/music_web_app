from django.forms import ModelForm
from django import forms
from .models import CommentDb

class NazarForm(ModelForm):
    comment = forms.CharField(label="نظر ", label_suffix="")
    class Meta:
        model=CommentDb
        fields = ("comment",)