# Generated by Django 4.1.3 on 2022-12-02 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0011_delete_fichatreino'),
    ]

    operations = [
        migrations.AddField(
            model_name='treino',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plataforma.aluno'),
            preserve_default=False,
        ),
    ]
