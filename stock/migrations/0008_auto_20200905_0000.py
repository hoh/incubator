# Generated by Django 3.0.9 on 2020-09-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20200904_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundzone',
            name='method',
            field=models.CharField(choices=[('BANK', 'Virement'), ('CASH', 'Caisse')], max_length=4),
        ),
    ]
