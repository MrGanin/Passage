# Generated by Django 5.0.6 on 2024-06-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_image_passage_alter_level_autumn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passage',
            name='connect',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='passage',
            name='other_titles',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
