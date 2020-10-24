from django.forms import ModelForm
from django import forms
from .models import CommentDb, Ahang

class NazarForm(ModelForm):
    comment = forms.CharField(label="نظر ", label_suffix="")
    user_name = forms.CharField(label="یوزر نیم", label_suffix="")
    email = forms.EmailField(label="ایمیل", label_suffix="")

    class Meta:
        model=CommentDb
        fields = ("comment","user_name", "email",)
        widgets = {"class":"form-control"}
class AhangUplaodingForm(ModelForm):
    author = forms.CharField(
        label="اسم خواننده",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder":"اسم خواننده", "class":"form-control"}
        ),
        required=False,
    )
    description = forms.CharField(
        label="متن اهنگ",
        label_suffix="",
        widget=forms.Textarea(
            attrs={"placeholder":"متن اهنگ", "class":"form-control"}
        ),
        required=True,    
    )
    ahang_esm = forms.CharField(
        label="اسم آهنگ",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder":"اسم آهنگ", "class":"form-control"}
        ),
        required=True,
    )
    ahang_file = forms.FileField(
        label="قایل آهنگ",
        label_suffix="",
        widget=forms.FileInput(
            attrs={"placeholder":"فایل آهنگ", "class":"form-control-file"}
        ),
        required=True,
    )
    class Meta:
        model = Ahang
        fields = ("author","description", "ahang_esm", "ahang_file",)