# Generated by Django 4.0.4 on 2022-07-20 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_watching'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watching',
            name='time',
            field=models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], default='M', max_length=1, verbose_name='Watch Time'),
        ),
    ]
