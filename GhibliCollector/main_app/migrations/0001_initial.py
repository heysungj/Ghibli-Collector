# Generated by Django 4.0.4 on 2022-07-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release', models.IntegerField()),
                ('director', models.TextField(max_length=100)),
                ('music', models.CharField(max_length=100)),
            ],
        ),
    ]
