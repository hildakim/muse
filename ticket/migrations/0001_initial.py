# Generated by Django 3.2 on 2021-08-09 13:06

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
                ('subject', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('p_date', models.DateTimeField()),
                ('contents', models.TextField()),
            ],
        ),
    ]
