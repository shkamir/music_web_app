from django.shortcuts import render, get_object_or_404, redirect
from .models import Ahang, CommentDb
from .forms import LoginForm, NazarForm, AhangUplaodingForm, SignUpForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login



def index(request):
    ahangha = Ahang.objects.all().order_by('-id')
    context = {
        "ahangha": ahangha,
        "title": "Home",
    }
    return render(request, 'main/index.html', context)

# def ahang_detail(request,id=None):
#     ahang = get_object_or_404(Ahang,id=id)
#     esme_ahang = f"{ahang.author}\t-\t{ahang.ahang_esm}"
    
#     # comment's
#     if request.method == "POST":
#         nazar = request.POST.get("cm")
#         CommentDb(comment=nazar).save()
#         #print (request.POST.get("cm"))
#     nazarat = CommentDb.objects.all()
#     context = {
#          "ahang":ahang, 
#          "nazarat": nazarat,
#          "title":esme_ahang,
#     }
#     return render(request,'main/ahang_detail.html',context)

def ahang_detail(request,id=None):
    
    
    
    ahang = get_object_or_404(Ahang,id=id, isAgreed=True)
    
    esme_ahang = f"{ahang.author}\t-\t{ahang.ahang_esm}"
    
    
    
    nazar_form = NazarForm()    
    # saving comments in (_  DB  _) comment's
    if request.method == "POST":
        nazar_form=NazarForm(request.POST)
        nazar_form.save()
        messages.success(request, ":) نظر شما با موفقیت ثبت شد  ")
        nazar_form = NazarForm()

    # showing the comments
    nazarat = CommentDb.objects.all()


    context = {
         "ahang":ahang, 
         "nazarat": nazarat,
         "nazar_form": nazar_form,
         "title":esme_ahang,
    }
    return render(request,'main/ahang_detail.html',context)


def upload_music_form(request):
    # ISSUE: file not uploading
    if request.method == "POST":
        form = AhangUplaodingForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "آهنگ شما با موفقیت ثبت شد و پس از بازرسی در سایت قرار میگیرد")
            form = AhangUplaodingForm()
            context = {
                "form": form
            }
            return render(request, "main/upload.html", context)
        context = {
            "form": form
        }
        return render(request, "main/upload.html", context)
    form = AhangUplaodingForm()
    context = {
        "form": form
    }
    return render(request, "main/upload.html", context)


def search(request):
    # gets q in address bar
    query = request.GET.get('q')
    button = request.GET.get('submitbutton')
    if query is not None:
        lookup = Q(author__icontains=query) | Q(description__icontains=query) | Q(ahang_esm__icontains=query)
        result = Ahang.objects.filter(lookup, isAgreed=True).distinct()
        context = {
            "result": result,
            "submit": button
        }
        return render(request, "main/search.html", context)
    return render(request, "main/search.html")


def register(request):
    """ handles user creation form """
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "با موفقیت ثبت شد :)")
            form = SignUpForm()
        else:
            messages.error(request, " :(  متاسفانه فرم شما ثبت نشد لطفا بعدا امتحان کنید")
            form = SignUpForm()
        
    return render(request, "main/signup.html", {"form":form})

    
    
def login_view(request):
    """ handle's User Login """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            messages.success(request, "با موفقیت ثبت شد :)")
            return redirect("music:home")
        else:
            messages.error(request, " :(  بعدا امتحان کنید")
            form = LoginForm()
            return render(request, 'main/login.html',{"form":form})

    form = LoginForm()    
    return render(request, 'main/login.html',{"form":form})
    