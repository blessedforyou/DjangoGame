# Generated by Django 5.1 on 2024-09-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='source',
            field=models.CharField(choices=[('level', 'Пройденный уровень'), ('manually', 'Вручную')], max_length=8, verbose_name='Источник получения'),
        ),
    ]
