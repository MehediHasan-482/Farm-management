# Generated by Django 4.2.5 on 2023-11-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_sno_contact_serial_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='protfolio',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]
