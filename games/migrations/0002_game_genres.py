# Generated by Django 4.0.3 on 2022-03-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(related_name='games', to='genres.genre'),
        ),
    ]
