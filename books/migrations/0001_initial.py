# Generated by Django 4.1.4 on 2022-12-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('jaquette', models.URLField(blank=True, max_length=1000, null=True)),
                ('editeur', models.CharField(blank=True, max_length=255, null=True)),
                ('collection', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('Librairie', models.CharField(blank=True, max_length=255, null=True)),
                ('date_emprut', models.DateField(blank=True, null=True)),
                ('date_retour', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
