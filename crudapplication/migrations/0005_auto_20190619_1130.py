# Generated by Django 2.1 on 2019-06-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapplication', '0004_auto_20190618_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eemail',
            field=models.EmailField(max_length=254),
        ),
    ]
