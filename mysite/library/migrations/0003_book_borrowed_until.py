# Generated by Django 3.2 on 2021-04-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
