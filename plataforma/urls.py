from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),

    #CRUD ALUNOS
    path('alunos/', views.alunos, name='alunos'),
    path('cadastro_aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('deletar_aluno/<int:id>/', views.deletar_aluno, name='deletar_aluno'),
    path('dados_aluno/<int:id>/', views.dados_aluno, name='dados_aluno'),
    path('editar_aluno/<int:id>/', views.editar_aluno, name='editar_aluno'),

    #FICHA DE TREINO
    path('ficha_treino/', views.ficha_treino, name='ficha_treino'),
    path('ficha_treino_id/<int:id>/', views.ficha_treino_id, name='ficha_treino_id'),


    path('grupos/', views.grupos, name='grupos'),
    path('grupo/<int:id>/', views.grupo, name='grupo'),
 
    #CRUD EXERCICIOS
    # BANCO DE EXERCICIO
    path('cadastro_exercicio/', views.cadastro_exercicio, name='cadastro_exercicio'),

    # EXERCICIO FICHA
    path('cadastro_exercicio_ficha/', views.cadastro_exercicio_ficha, name='cadastro_exercicio_ficha'),
    path('deletar_exercicio_ficha/<int:id>/', views.deletar_exercicio_ficha, name='deletar_exercicio_ficha'),


    #CRUD TREINO
    path('cadastro_treino/', views.cadastro_treino, name='cadastro_treino'),
]
