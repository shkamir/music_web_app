from django.forms import ModelForm
from django import forms
from .models import CommentDb

class NazarForm(ModelForm):
    comment = forms.CharField(label="نظر ", label_suffix="")
    user_name = forms.CharField(label="یوزر نیم", label_suffix="")
    email = forms.EmailField(label="ایمیل", label_suffix="")

    class Meta:
        model=CommentDb
        fields = ("comment","user_name", "email",)
        widgets = {"class":"form-control"}
