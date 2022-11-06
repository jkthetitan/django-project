from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Doctor(models.Model):
    date_of_birth =	models.DateField('Date of birth')
    iin =       	models.CharField('IIN numer', max_length=12, validators=[MinLengthValidator(12)], unique=True)
    id =	    	models.CharField('ID number', max_length=9, validators=[MinLengthValidator(9)], unique=True, primary_key=True)
    first_name =	models.CharField('First Name', max_length=50)
    middle_name =	models.CharField('Middle Name', max_length=50, blank=True)
    last_name =     models.CharField('Last Name', max_length=50)
    contact_number= PhoneNumberField('Contact Number', region='KZ' ) #remove blank=True
    department_id = models.CharField('Department Number', max_length=4, validators=[MinLengthValidator(4)])
    specializtion_id = models.CharField('Specialization Number', max_length=4, validators=[MinLengthValidator(4)])
    experience_years = models.IntegerField('Experience in years', validators=[MinValueValidator(0), MaxValueValidator(50)])
    photo = models.ImageField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    schedule_detials = models.TextField(blank=True)
    DEGREE_TYPE = [
        ('none', 'none'), ('associate', 'associate'), ('bachelor’s', 'bachelor’s'), ('graduate', 'graduate'), ('doctorate', 'doctorate'), ('professional', 'professional'),
    ]
    degree = models.CharField('Degree Type', max_length=20, choices=DEGREE_TYPE, default='none')
    rating = models.IntegerField('Rating', validators=[MinValueValidator(0), MaxValueValidator(10)])
    address = models.CharField(max_length=256)
    homepage_url = models.URLField(blank=True)