# Generated by Django 4.2 on 2024-03-03 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]