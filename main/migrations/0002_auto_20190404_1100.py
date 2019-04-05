# Generated by Django 2.0.13 on 2019-04-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player3',
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='main.Player'),
        ),
    ]