# Generated by Django 4.2.3 on 2023-09-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_alter_customer_typeperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='TypePerson',
            field=models.CharField(blank=True, default='Customer', max_length=200),
        ),
    ]
