from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'home.html')


def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos':alunos})


def grupos(request):
    grupos = GrupoMuscular.objects.all()
    return render(request, 'grupos.html', {'grupos': grupos})

def execicio_id(request, id):
    exercicios_id = Exercicio.objects.filter(grupo_muscular=id)
    return render(request, 'exercicios_id.html', {'exercicios_id':exercicios_id})