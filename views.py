from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse('<h1>Lokesh yadav<h1>')



def magic(request):
    print('lokesh')
    return render(request , 'magic.html')


def signup(request):
    return render(request , 'signup.html')