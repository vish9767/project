# Generated by Django 4.2.1 on 2023-07-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0007_remove_agg_hhc_professional_scheduled_professiona_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agg_hhc_professional_scheduled',
            name='from_time',
            field=models.DateTimeField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='agg_hhc_professional_scheduled',
            name='to_time',
            field=models.DateTimeField(max_length=240, null=True),
        ),
    ]
