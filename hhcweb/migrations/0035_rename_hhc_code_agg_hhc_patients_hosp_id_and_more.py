# Generated by Django 4.2.2 on 2023-07-05 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0034_alter_agg_hhc_patients_hhc_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agg_hhc_patients',
            old_name='hhc_code',
            new_name='hosp_id',
        ),
        migrations.RemoveField(
            model_name='agg_hhc_patients',
            name='Hospital_name',
        ),
    ]
