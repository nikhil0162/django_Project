# Generated by Django 2.1.4 on 2019-02-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpost',
            name='gender',
            field=models.BooleanField(default=False),
        ),
    ]