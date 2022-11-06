# Generated by Django 4.0.6 on 2022-11-05 23:22

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_blood_group_alter_patient_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='KZ'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('O-', 'Negative Group O'), ('O+', 'Positive Group O'), ('A-', 'Negative Group A'), ('A+', 'Positive Group A'), ('B-', 'Negative Group B'), ('B+', 'Positive Group B'), ('AB-', 'Negative Group AB'), ('AB+', 'Positive Group AB')], default='O+', max_length=3, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Blood Group'),
        ),
    ]