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
    a = Aluno.objects.get(id=2)
    print(a.data_nascimento)
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


# CRUD CADASTRO EXERCICIOS

def cadastro_exercicio(request):
    if request.method == 'POST':
        exercicio = request.POST.get('exercicio')
        musculo = request.POST.get('musculo')
        
        grupo_muscular = GrupoMuscular.objects.get(id=musculo)

        novo_exercicio = BancoExercicios(nome=exercicio,grupo_muscular=grupo_muscular)

        novo_exercicio.save()
        return redirect(f'/grupo/{musculo}')


def cadastro_treino(request):
    if request.method == 'POST':
        aluno = request.POST.get('aluno')
        treino = request.POST.get('treino')

        al = Aluno.objects.get(id=aluno)

        novo_treino = Treino(aluno=al, nome=treino)
        novo_treino.save()
        return redirect(f'/ficha_treino_id/{aluno}')


# CRUD CADASTRO EXERCICIOS FICHA ALUNO

def cadastro_exercicio_ficha(request):
    if request.method == 'POST':
        exercicio = request.POST.get('exercicio')
        treino = request.POST.get('treino')
        series = request.POST.get('series')
        tecnica = request.POST.get('tecnica')

    exe = BancoExercicios.objects.get(id=exercicio)
    treino = Treino.objects.get(id=treino)

    novo_exercicio = Exercicio(exercicio=exe, treino=treino, series=series, tecnica=tecnica)

    novo_exercicio.save()
    return redirect(f'/ficha_treino_id/{treino.aluno_id}')



def grupos(request):
    grupos = GrupoMuscular.objects.all()
    return render(request, 'grupos.html', {'grupos': grupos})

def grupo(request, id):
    exercicios = BancoExercicios.objects.filter(grupo_muscular_id=id)
    i = GrupoMuscular.objects.get(id=id)
    return render(request, 'grupo_id.html', {'exercicios':exercicios, 'i':i})


# def exercicio(request,id):
#     exercicios = BancoExercicios.objects.filter(grupo_muscular_id=id)
#     return render(request, 'exercicios.html',{'exercicios':exercicios})



def ficha_treino(request):
    alunos = Aluno.objects.all()
    return render(request, 'ficha_treino.html', {'alunos': alunos})


def ficha_treino_id(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'GET':
    
        treinos = Treino.objects.filter(aluno=aluno)

        exercicios = Exercicio.objects.all()

        banco_exe = BancoExercicios.objects.all()

        return render(request, 'ficha_treino_id.html', {'aluno':aluno, 'treinos': treinos, 'exercicios':exercicios, 'banco_exe': banco_exe})
