# Generated by Django 4.1.3 on 2022-12-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0016_alter_exercicio_exercicio_alter_exercicio_treino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='treino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plataforma.treino'),
            preserve_default=False,
        ),
    ]
