# Generated by Django 4.1.3 on 2022-11-30 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Maculino')], max_length=1)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('repeticoes', models.CharField(max_length=50)),
                ('tecnica', models.CharField(blank=True, max_length=10, null=True)),
                ('video', models.FileField(upload_to='video')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.aluno')),
            ],
        ),
    ]
