# Generated by Django 4.2.5 on 2023-11-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='cow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('age', models.IntegerField()),
                ('weight', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('per_kg_cost', models.IntegerField()),
                ('description', models.CharField(default='Default Description', max_length=200)),
                ('pic', models.ImageField(default='', upload_to=None)),
            ],
        ),
    ]
