# Generated by Django 3.0.2 on 2020-01-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_shipment_details_isreviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier_details',
            name='SuppCode',
            field=models.IntegerField(),
        ),
    ]
