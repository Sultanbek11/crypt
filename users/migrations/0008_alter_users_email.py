# Generated by Django 4.1.3 on 2023-08-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
    ]
