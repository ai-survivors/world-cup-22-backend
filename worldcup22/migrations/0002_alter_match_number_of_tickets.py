# Generated by Django 4.0 on 2021-12-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup22', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='number_of_tickets',
            field=models.IntegerField(),
        ),
    ]
