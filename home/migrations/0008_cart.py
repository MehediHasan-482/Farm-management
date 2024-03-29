# Generated by Django 4.2.5 on 2023-12-02 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_protfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cow')),
            ],
        ),
    ]
