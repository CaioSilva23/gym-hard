from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('alunos/', views.alunos, name='alunos'),
    path('grupos/', views.grupos, name='grupos'),
    path('execicio_id/<int:id>/', views.execicio_id, name='execicio_id'),
]
