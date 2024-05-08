# Generated by Django 5.0.6 on 2024-05-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_actuel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subgoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
    ]