# Generated by Django 4.2 on 2024-03-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
