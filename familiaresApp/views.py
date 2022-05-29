from django.shortcuts import render
from .models import Familiares

# Create your views here.
def familiares(request):
    familiares_list = Familiares.objects.all
    return render(request, 'familiares.html', {'familiares': familiares_list})
