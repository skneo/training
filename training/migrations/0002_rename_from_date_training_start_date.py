# Generated by Django 5.1.1 on 2024-09-05 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='from_date',
            new_name='start_date',
        ),
    ]
