# Generated by Django 4.1.6 on 2023-02-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='category',
            field=models.CharField(choices=[('q', 'Pytanie'), ('o', 'Inne')], max_length=10),
        ),
    ]
