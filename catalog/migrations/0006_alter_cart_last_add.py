# Generated by Django 5.1.6 on 2025-03-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_customer_email_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='last_add',
            field=models.DateTimeField(null=True),
        ),
    ]
