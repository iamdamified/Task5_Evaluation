# Generated by Django 5.1.7 on 2025-03-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('candidate', models.CharField(max_length=100)),
                ('scores', models.FloatField()),
                ('comment', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
