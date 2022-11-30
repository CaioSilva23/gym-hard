from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'home.html')


def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos':alunos})
