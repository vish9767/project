# Generated by Django 4.2.2 on 2023-07-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0004_remove_agg_hhc_events_pt_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agg_hhc_events',
            name='event_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
