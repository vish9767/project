# Generated by Django 4.2.2 on 2023-06-14 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhcweb', '0022_agg_hhc_patient_documents_delete_agg_hhc_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agg_hhc_patient_documents',
            name='agg_sp_pt_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hhcweb.agg_hhc_patients'),
        ),
        migrations.AlterField(
            model_name='agg_hhc_patient_documents',
            name='doucment',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]