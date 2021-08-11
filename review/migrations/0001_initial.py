# Generated by Django 3.2.6 on 2021-08-11 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mt20id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('upload_date', models.DateTimeField()),
                ('view_date', models.DateField()),
                ('view_time', models.TimeField(blank=True, null=True)),
                ('cast1', models.CharField(max_length=10)),
                ('cast2', models.CharField(blank=True, max_length=10, null=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='review/%Y/%m/%d/')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
