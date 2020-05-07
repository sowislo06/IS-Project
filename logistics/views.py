from django.shortcuts import render


def index(request):
    return render(request, 'logistics/base.html')
