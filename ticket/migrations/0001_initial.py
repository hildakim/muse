# Generated by Django 3.2.6 on 2021-08-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('contents', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='ticket/')),
            ],
        ),
    ]
