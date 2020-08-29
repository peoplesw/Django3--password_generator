from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html') #views is going to look in the templates directory in the same directory as itself

def aboutme(request):
    return render(request, 'generator/aboutme.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
# checkboxes
    if request.GET.get('uppercase') == 'on':
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special') == 'on':
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers') == 'on':
        characters.extend(list('0123456789'))
# length
    length = int(request.GET.get('length', 12))
# creating the password from the characters in the "characters" list
    thepassword = ''
    for num in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword}) #views is going to look in the templates directory in the same directory as itself
