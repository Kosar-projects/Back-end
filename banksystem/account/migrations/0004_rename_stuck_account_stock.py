# Generated by Django 4.2 on 2024-08-08 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_owener_account_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='stuck',
            new_name='stock',
        ),
    ]
