from django.shortcuts import render
from .models import Card

# Create your views here.
def index(request):

    card = Card.objects.all()

    context = {
        'card': card,
    }
    
    return render(request, 'home/index.html', context)