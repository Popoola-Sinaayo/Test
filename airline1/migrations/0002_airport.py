# Generated by Django 3.0.8 on 2020-07-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
    ]
