# Generated by Django 2.1.4 on 2019-02-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190204_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpost',
            name='company_name',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='carpost',
            name='model_name',
            field=models.BooleanField(),
        ),
    ]