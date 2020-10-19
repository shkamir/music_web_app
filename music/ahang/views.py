from django.shortcuts import render
from .models import Ahang


def index(request):
    ahangha = Ahang.objects.all()
    context = {
        "ahangha": ahangha,
    }
    return render(request, 'main/index.html', context)
