from django.db import models
from datetime import date

# Create your models here.
class Aluno(models.Model):
    choices_sexo = (('F', 'Feminino'),
    ('M', 'Maculino'))

    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    # personal = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    paciente = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateTimeField()
    peso = models.IntegerField()
    altura = models.IntegerField()

    def __str__(self) -> str:
        return f'Dados: {self.paciente} - {self.peso}'




class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome

class BancoExercicios(models.Model):
    nome = models.CharField(max_length=25)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.SET_NULL, null=True)


class Exercicio(models.Model):
    exercio = models.ManyToManyField(BancoExercicios)
    nome = models.CharField(max_length=50)
    video = models.FileField(upload_to='video', null=True, blank=True)
    series = models.CharField(max_length=10)
    tecnica = models.CharField(max_length=25, null=True, blank=True)



    def __str__(self):
        return self.nome

class Treino(models.Model):
    nome = models.CharField(max_length=10)
     

    def __str__(self) -> str:
        return self.nome



class FichaTreino(models.Model):
    treino_chices = (('ABC','ACB'),('AB','AB'))
    treinos = models.ForeignKey(Treino, on_delete=models.SET_NULL, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipo_treino = models.CharField(max_length=3, choices=treino_chices)
    dias = models.IntegerField()
    data_inicio = models.DateField(default=date.today())

    def __str__(self) -> str:
        return f'Ficha {self.aluno}'
    

