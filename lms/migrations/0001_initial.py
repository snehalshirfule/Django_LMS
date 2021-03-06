# Generated by Django 3.2.7 on 2021-11-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('ISBN', models.BigIntegerField()),
                ('country_of_origin', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
