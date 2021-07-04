# Generated by Django 3.2.5 on 2021-07-04 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj2', '0002_auto_20210704_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating_website',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='final_comment',
            field=models.TextField(default='', max_length=400, null=True),
        ),
    ]
