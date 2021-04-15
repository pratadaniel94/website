from django.shortcuts import render
from core.models import Apoiadores

# Create your views here.

def index(request):
    return render(request, "index.html")


def get_supporters(request):
    context = {
        "apoiadores": Apoiadores.objects.all(),
        "img_default": "/static/media/profile/default.png"
    }
    return render(request, "parceiros.html", context)