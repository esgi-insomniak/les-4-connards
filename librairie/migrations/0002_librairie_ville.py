# Generated by Django 4.0.8 on 2023-01-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librairie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='librairie',
            name='ville',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]