# Generated by Django 4.2 on 2024-08-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_stuck_account_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='stock',
            field=models.BigIntegerField(db_index=True),
        ),
    ]
