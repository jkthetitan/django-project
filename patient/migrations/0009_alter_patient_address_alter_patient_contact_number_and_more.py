# Generated by Django 4.0.6 on 2022-11-06 13:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_alter_patient_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KZ', verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KZ', verbose_name='Emergency Contact Number'),
        ),
    ]
