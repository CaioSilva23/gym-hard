# Generated by Django 4.1.3 on 2022-12-02 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_remove_exercicio_grupo_muscular_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercicio',
            old_name='exercio',
            new_name='exercicio',
        ),
        migrations.RemoveField(
            model_name='exercicio',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='exercicio',
            name='video',
        ),
    ]