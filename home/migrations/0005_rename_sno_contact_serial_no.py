# Generated by Django 4.2.5 on 2023-11-24 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sno',
            new_name='serial_no',
        ),
    ]
