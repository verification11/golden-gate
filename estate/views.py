from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def housing(request):
    return render(request, 'housing.html')

def about(request):
    return render(request, 'about.html')