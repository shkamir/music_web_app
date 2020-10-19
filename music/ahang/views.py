from django.shortcuts import render, get_object_or_404
from .models import Ahang


def index(request):
    ahangha = Ahang.objects.all()
    context = {
        "ahangha": ahangha,
    }
    return render(request, 'main/index.html', context)

def ahang_detail(request, id=None):
    ahang = get_object_or_404(Ahang, id=id)
    return render(request,'main/ahang_detail.html', {"ahang":ahang})