# Generated by Django 4.2.1 on 2023-06-07 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0017_agg_hhc_app_caller_register_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agg_hhc_patients',
            name='app_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hhcweb.agg_hhc_app_caller_register'),
        ),
    ]
