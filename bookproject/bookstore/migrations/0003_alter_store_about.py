# Generated by Django 3.2.7 on 2021-09-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_store_bookimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='about',
            field=models.CharField(max_length=1000),
        ),
    ]
