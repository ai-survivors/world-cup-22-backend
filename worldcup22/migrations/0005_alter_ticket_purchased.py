# Generated by Django 4.0 on 2021-12-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup22', '0004_ticket_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]