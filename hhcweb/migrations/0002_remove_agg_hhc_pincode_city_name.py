# Generated by Django 4.2.1 on 2023-07-12 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agg_hhc_pincode',
            name='city_name',
        ),
    ]
