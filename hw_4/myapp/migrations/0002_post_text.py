# Generated by Django 4.1.2 on 2022-10-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
