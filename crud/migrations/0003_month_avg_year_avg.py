# Generated by Django 3.2.4 on 2021-07-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210707_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month_avg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('month', models.CharField(max_length=25, verbose_name='Месяц')),
                ('year', models.IntegerField()),
                ('temperature_avg', models.FloatField()),
                ('humidity_avg', models.FloatField()),
                ('windspeed_avg', models.FloatField()),
            ],
            options={
                'verbose_name': 'Среднее значение за месяц',
                'verbose_name_plural': 'Средние значения за месяцы',
            },
        ),
        migrations.CreateModel(
            name='Year_avg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('year', models.IntegerField()),
                ('temperature_avg', models.FloatField()),
                ('humidity_avg', models.FloatField()),
                ('windspeed_avg', models.FloatField()),
            ],
            options={
                'verbose_name': 'Среднее значение за год',
                'verbose_name_plural': 'Средние значения за годы',
            },
        ),
    ]
