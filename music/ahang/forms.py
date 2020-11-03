from django.forms import ModelForm
from django import forms
from .models import CommentDb, Ahang
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class NazarForm(ModelForm):
    """ contact form """
    comment = forms.CharField(label="نظر ", label_suffix="")
    user_name = forms.CharField(label="یوزر نیم", label_suffix="")
    email = forms.EmailField(label="ایمیل", label_suffix="")

    class Meta:
        model=CommentDb
        fields = ("comment","user_name", "email",)
        widgets = {"class":"form-control"}
class AhangUplaodingForm(ModelForm):
    """ let user upload a music """
    author = forms.CharField(
        label="اسم خواننده",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder":"اسم خواننده", "class":"form-control"}
        ),
        required=True,
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
    
    def clean_ahang_file(self):
        # ISSUE: getting error even file has mp3 ext
        ahang = self.cleaned_data.get("ahang_file")
        mp3 = ".mp3"
        if not mp3 in ahang:
            print (ahang)
            raise forms.ValidationError("فرمت فایل مناسب نیست")
        return ahang


class SignUpForm(UserCreationForm):
    """ register's a user """
    first_name = forms.CharField(
        label=" اسم",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder":"اسم ", "class":"form-control"}
        ),
        required=True,
    )
    username = forms.CharField(
        label=" نام کاربری",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder":"نام کاربری ", "class":"form-control"}
        ),
        required=True,
    )
    email = forms.EmailField(
        label=" ایمیل",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"placeholder":"ایمیل ", "class":"form-control"}
        ),
        required=True,
    )
    password1 = forms.CharField(
        label=" گذر واژه",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"placeholder":"گذر واژه ", "class":"form-control"}
        ),
        required=True,
    )
    
    password2 = forms.CharField(
        label="  تایید گذر واژه",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"placeholder":"  تایید گذر واژه ", "class":"form-control"}
        ),
        required=True,
    )
    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "email",
            "password1",
            "password2",
        )
        help_texts = {
            "username": None
        }
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=" نام کاربری",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder":"نام کاربری ", "class":"form-control"}
        ),
        required=True,
    )
    password = forms.CharField(
        label=" گذر واژه",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"placeholder":"گذر واژه ", "class":"form-control"}
        ),
        required=True,
    )
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )    
    
    
    
