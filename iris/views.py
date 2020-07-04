from django.shortcuts import render

# Create your views here.
def iris(request):
    return render(request, 'iris.html')