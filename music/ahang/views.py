from django.shortcuts import render, get_object_or_404
from .models import Ahang, CommentDb


def index(request):
    ahangha = Ahang.objects.all().order_by('-id')
    context = {
        "ahangha": ahangha,
        "title": "Home",
    }
    return render(request, 'main/index.html', context)

def ahang_detail(request,id=None):
    ahang = get_object_or_404(Ahang,id=id)
    esme_ahang = f"{ahang.author}\t-\t{ahang.ahang_esm}"
    
    # comment's
    if request.method == "POST":
        nazar = request.POST.get("cm")
        CommentDb(comment=nazar).save()
        #print (request.POST.get("cm"))
    nazarat = CommentDb.objects.all()
    context = {
         "ahang":ahang, 
         "nazarat": nazarat,
         "title":esme_ahang,
    }
    return render(request,'main/ahang_detail.html',context)
