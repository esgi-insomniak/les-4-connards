# Generated by Django 4.0.8 on 2023-01-02 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_loan_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='returned',
        ),
    ]
