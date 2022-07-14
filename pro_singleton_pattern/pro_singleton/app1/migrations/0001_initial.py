# Generated by Django 4.0.4 on 2022-04-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('sal', models.FloatField()),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]