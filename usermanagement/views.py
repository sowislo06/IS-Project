from django.shortcuts import render

#Method 'index'
def index(request):
    return render(request, 'usermanagement/base.html')
