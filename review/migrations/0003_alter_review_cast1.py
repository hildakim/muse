# Generated by Django 3.2.6 on 2021-08-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cast1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
