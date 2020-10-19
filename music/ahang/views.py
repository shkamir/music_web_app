from django.shortcuts import render, get_object_or_404
from .models import Ahang


def index(request):
    ahangha = Ahang.objects.all().order_by('-updateDate')
    context = {
        "ahangha": ahangha,
        "title": "Home",
    }
    return render(request, 'main/index.html', context)

def ahang_detail(request, id=None):
    ahang = get_object_or_404(Ahang, id=id)
    esme_ahang = f"{ahang.author}\t------\t{ahang.ahang_esm}"
    return render(request,'main/ahang_detail.html', {"ahang":ahang, "title":esme_ahang})
