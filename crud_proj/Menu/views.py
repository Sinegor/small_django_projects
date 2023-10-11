from django.shortcuts import render
from .models import Menu_model

def index (request, menu, title, headline):


    return render(request, 'Menu/main.html', {'title':title, 'type_menu': menu, 'headline':headline})

