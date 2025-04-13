from django.shortcuts import render


def index(request):
    name = "World"
    return render(request, "base.html", {"name": name})

# Create your views here.