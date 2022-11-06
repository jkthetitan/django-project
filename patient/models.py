from django.db import models
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
# Create your models here.

class Patient(models.Model):
    date_of_birth =	models.DateField('Date of birth')
    iin =       	models.CharField('IIN numer', max_length=12, validators=[MinLengthValidator(12)], unique=True)
    id =	    	models.CharField('ID number', max_length=9, validators=[MinLengthValidator(9)], unique=True, primary_key=True)
    first_name =	models.CharField('First Name', max_length=50)
    middle_name =	models.CharField('Middle Name', max_length=50, blank=True)
    last_name =     models.CharField('Last Name', max_length=50)

    FIRST_NEG = 'O-'
    FIRST_POS = 'O+'
    SECOND_NEG = 'A-'
    SECOND_POS = 'A+'
    THIRD_NEG = 'B-'
    THIRD_POS = 'B+'
    FOURTH_NEG = 'AB-'
    FOURTH_POS = 'AB+'

    BLOOD_GROUP = [
        (FIRST_POS, FIRST_POS), (FIRST_NEG, FIRST_NEG),
        (SECOND_POS, SECOND_POS), (SECOND_NEG, SECOND_NEG),
        (THIRD_POS, THIRD_POS), (THIRD_NEG, THIRD_NEG),
        (FOURTH_POS, FOURTH_POS), (FOURTH_NEG, FOURTH_NEG),
    ]
    blood_group =   models.CharField('Blood Group', max_length=3, validators=[MinLengthValidator(2)], choices=BLOOD_GROUP, default=FIRST_POS)
    emergency_contact_number = PhoneNumberField('Emergency Contact Number', region='KZ') #remove blank=True
    contact_number = PhoneNumberField('Contact Number', region='KZ' ) #remove blank=True
    email = models.EmailField(max_length=254, blank=True) #optional attribute
    address = models.CharField(max_length=256) #remove blank=True

    MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced'),
    ]
    marital_status = models.CharField('Marital Status', choices=MARITAL_STATUS, max_length=15, default='Single')
    registration_date = models.DateField('Registration Date', default=date.today)
    comments = models.TextField(blank=True)



