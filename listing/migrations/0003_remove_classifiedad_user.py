# Generated by Django 5.0.6 on 2024-07-12 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_remove_classifiedad_company_delete_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classifiedad',
            name='user',
        ),
    ]
