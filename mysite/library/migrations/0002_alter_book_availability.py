# Generated by Django 3.2 on 2021-04-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.BooleanField(),
        ),
    ]
