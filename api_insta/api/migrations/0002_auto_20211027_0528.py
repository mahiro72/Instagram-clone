# Generated by Django 3.0.7 on 2021-10-26 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_pn',
            new_name='created_on',
        ),
    ]
