from django.shortcuts import render
from core.models import Apoiadores

# Create your views here.


def index(request):
    context = {
        "apoiadores": Apoiadores.objects.all()
    }
    return render(request, "base.html", context)