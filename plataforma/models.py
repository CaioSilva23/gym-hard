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
    
    def __str__(self):
        return self.nome

class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
     

    def __str__(self) -> str:
        return self.nome


class Exercicio(models.Model):
    exercicio = models.ForeignKey(BancoExercicios, on_delete=models.SET_NULL, null=True)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    series = models.CharField(max_length=10)
    tecnica = models.CharField(max_length=25, null=True, blank=True)


    def __str__(self):
        return f'{self.exercicio}'



    

