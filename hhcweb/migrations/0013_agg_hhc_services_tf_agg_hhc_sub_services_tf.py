# Generated by Django 4.2.1 on 2023-05-31 05:22

from django.db import migrations
import django_enumfield.db.fields
import hhcweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0012_remove_agg_hhc_services_s1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agg_hhc_services',
            name='tf',
            field=django_enumfield.db.fields.EnumField(default=1, enum=hhcweb.models.Tf_enum),
        ),
        migrations.AddField(
            model_name='agg_hhc_sub_services',
            name='tf',
            field=django_enumfield.db.fields.EnumField(default=1, enum=hhcweb.models.Tf_enum),
        ),
    ]
