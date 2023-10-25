# Generated by Django 4.2.6 on 2023-10-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
            ],
        ),
    ]
