from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# CRUD ALUNOS

def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos':alunos})

def cadastro_aluno(request):

    if request.method == 'GET':
        return redirect('/alunos/')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        nascimento = request.POST.get('nascimento')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        try:
            novo_aluno = Aluno(nome=nome,sexo=sexo,data_nascimento=nascimento,email=email, telefone=telefone)
            novo_aluno.save()
            messages.add_message(request,constants.SUCCESS,'Aluno cadastrado com sucesso!')
            return redirect('/alunos/')
        except Exception as e:
            print(e)
            messages.add_message(request,constants.ERROR,'Erro ao cadastrar aluno!')

            return redirect('/alunos/')


def editar_aluno(request,id):
    if request.method == 'POST':
        try:
                
            aluno = Aluno.objects.get(id=id)

            nome = request.POST.get('nome')
            sexo = request.POST.get('sexo')
            nascimento = request.POST.get('nascimento')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')

            aluno.nome = nome
            aluno.sexo = sexo
            aluno.data_nascimento = nascimento
            aluno.email = email
            aluno.telefone = telefone

            aluno.save()
            return redirect(f'/dados_aluno/{id}')
        except Exception as e:
            print(e)
            return redirect(f'/dados_aluno/{id}')

def dados_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'dados_aluno.html',{'aluno':aluno})




def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('/alunos/')





def grupos(request):
    grupos = GrupoMuscular.objects.all()
    return render(request, 'grupos.html', {'grupos': grupos})

def grupo(request, id):
    grupo = Exercicio.objects.filter(grupo_muscular=id)
    return render(request, 'grupo_id.html', {'grupo':grupo})