# Generated by Django 2.2.1 on 2019-05-26 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0003_text_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='document',
        ),
        migrations.RemoveField(
            model_name='text',
            name='msg',
        ),
    ]