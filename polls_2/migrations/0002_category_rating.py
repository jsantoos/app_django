# Generated by Django 3.2 on 2022-08-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rating',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
