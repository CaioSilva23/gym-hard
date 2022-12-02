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


    path('grupos/', views.grupos, name='grupos'),
    path('grupo/<int:id>/', views.grupo, name='grupo'),
]
