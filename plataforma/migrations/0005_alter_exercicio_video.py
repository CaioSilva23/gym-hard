# Generated by Django 4.1.3 on 2022-11-30 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_grupomuscular_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
    ]
