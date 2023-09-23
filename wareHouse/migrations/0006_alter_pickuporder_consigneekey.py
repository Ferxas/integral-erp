# Generated by Django 4.2.3 on 2023-09-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_alter_consignee_vendorid'),
        ('wareHouse', '0005_alter_pickuporder_pickuplocationkey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuporder',
            name='consigneekey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='consigneekey', to='maintenance.customer'),
        ),
    ]