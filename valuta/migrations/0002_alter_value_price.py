# Generated by Django 4.1.3 on 2022-12-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valuta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=15, max_length=50, null=True),
        ),
    ]