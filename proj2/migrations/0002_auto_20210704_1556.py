# Generated by Django 3.2.5 on 2021-07-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_name', models.CharField(max_length=60)),
                ('final_comment', models.TextField(max_length=400, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_birth',
            field=models.DateTimeField(),
        ),
    ]
