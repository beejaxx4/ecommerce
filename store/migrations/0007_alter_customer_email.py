# Generated by Django 4.0.4 on 2022-07-22 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]