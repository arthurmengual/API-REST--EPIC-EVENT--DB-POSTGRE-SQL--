# Generated by Django 4.0.3 on 2022-03-20 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_contract_client_remove_contract_sales_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]