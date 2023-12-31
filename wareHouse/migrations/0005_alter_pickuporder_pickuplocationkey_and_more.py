# Generated by Django 4.2.3 on 2023-09-15 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_alter_customer_typeperson'),
        ('wareHouse', '0004_alter_pickuporder_issuedbykey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuporder',
            name='PickUpLocationkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pickUpLocation', to='maintenance.customer'),
        ),
        migrations.AlterField(
            model_name='pickuporder',
            name='shipperkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipper', to='maintenance.customer'),
        ),
    ]
