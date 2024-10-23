# Generated by Django 4.0.3 on 2022-10-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_rename_quanytity_quotation_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead_activity',
            name='actual_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='lead_activity',
            name='demo_status',
            field=models.CharField(choices=[('1', 'Pending'), ('3', 'Completed')], default='1', max_length=10),
        ),
    ]