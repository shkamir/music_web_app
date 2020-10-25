from django.shortcuts import render, get_object_or_404, redirect
from .models import Ahang, CommentDb
from .forms import NazarForm, AhangUplaodingForm
from django.contrib import messages
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
    
    
    
    ahang = get_object_or_404(Ahang,id=id)
    
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
        form = AhangUplaodingForm(request.POST or None)
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