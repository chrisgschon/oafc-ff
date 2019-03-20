# Generated by Django 2.0.13 on 2019-03-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=200)),
                ('position', models.CharField(default='None', max_length=200)),
                ('goals', models.PositiveIntegerField()),
                ('assists', models.PositiveIntegerField()),
                ('owngoals', models.PositiveIntegerField()),
                ('cleansheets', models.PositiveIntegerField()),
                ('yellowcards', models.PositiveIntegerField()),
                ('redcards', models.PositiveIntegerField()),
                ('motms', models.PositiveIntegerField()),
                ('points', models.PositiveIntegerField()),
            ],
        ),
    ]
