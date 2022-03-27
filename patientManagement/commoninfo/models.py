from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_birthyear(value):
    """Raises ValidationError if year chosen is past the current year"""
    if value.year > datetime.date().year:
        raise ValidationError(f"{value.year} is not a valid birth year.")

letters = RegexValidator(r'^[a-zA-Z]*$', "This field should only contain letters.")
nums = RegexValidator(r'^[0-9]*$', "Phone number should only contain numbers.")

class Patient(models.Model):
    unique_id = models.CharField(max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100, validators=[letters], help_text="Enter patient's first name: ")
    last_name = models.CharField(max_length=100, validators=[letters])
    date_of_birth = models.DateField(validators=[validate_birthyear])
    address = models.CharField(max_length=40, help_text="Enter the first line of patient's address: ")
    city = models.CharField(default="null", max_length=20, validators=[letters])
    state = models.CharField(default="null", max_length=20, validators=[letters])
    postcode = models.CharField(default="null", max_length=8)
    phone = models.CharField(max_length=14, validators=[nums], help_text="Enter the patient's phone number: ")
    email = models.EmailField(max_length=50, blank='True', help_text="Enter the patient's email address: ")

    class Meta: 
        ordering = ['unique_id', 'first_name', 'last_name', 'date_of_birth', 'address', 'postcode', 'phone', 'email']

    def get_absolute_url(self): 
        """Returns the url to access a particular instance of Patient"""
        return reverse('patient-details', args=[str(self.primary_key)])

    def __str__(self): 
        return f'{self.unique_id}, {self.first_name} {self.last_name}, {self.date_of_birth}, {self.address}, {self.postcode}, {self.phone}, {self.email}'

