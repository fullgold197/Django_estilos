from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def saludo(request):
    return render(request, 'saludo.html')

def penultimo(request):
    return render(request, 'penultimo.html')

def ultimo(request):
    return render(request, 'ultimo.html')
    

