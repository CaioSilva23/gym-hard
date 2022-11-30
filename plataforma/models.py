from django.db import models

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

class Exercicio(models.Model):
    nome = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    repeticoes = models.CharField(max_length=50)
    tecnica = models.CharField(max_length=10, null=True, blank=True)
    video = models.FileField(upload_to='video')


    def __str__(self):
        return self.titulo
