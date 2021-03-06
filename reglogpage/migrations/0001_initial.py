# Generated by Django 2.1.3 on 2018-12-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempHumdity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_temperature', models.IntegerField()),
                ('min_temperature', models.IntegerField()),
                ('max_humidity', models.IntegerField()),
                ('min_humidity', models.IntegerField()),
            ],
            options={
                'ordering': ['max_temperature'],
            },
        ),
    ]
