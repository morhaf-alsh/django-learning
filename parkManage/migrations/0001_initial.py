# Generated by Django 4.2.4 on 2023-08-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('car_type', models.CharField(choices=[('light vehicle', 'light vehicle'), ('meduim vehicle', 'meduim vehicle'), ('heavy vehicle', 'heavy vehicle')], default='light vehicle', max_length=50)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
            ],
        ),
    ]
