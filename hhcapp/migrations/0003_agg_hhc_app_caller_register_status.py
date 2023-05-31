# Generated by Django 4.2.1 on 2023-05-31 09:02

from django.db import migrations
import django_enumfield.db.fields
import hhcweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('hhcapp', '0002_agg_hhc_app_caller_register_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agg_hhc_app_caller_register',
            name='status',
            field=django_enumfield.db.fields.EnumField(enum=hhcweb.models.active_inactive_enum, null=True),
        ),
    ]
