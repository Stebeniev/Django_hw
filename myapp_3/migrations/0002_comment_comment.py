# Generated by Django 4.1.2 on 2022-10-25 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='myapp_3.comment'),
        ),
    ]
