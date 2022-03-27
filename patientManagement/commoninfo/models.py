from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_birthyear(value):
    """Raises ValidationError if year chosen is past the current year"""
    if value > datetime.date.today():
        raise ValidationError(f"{value} is not a valid birthday.")

letters = RegexValidator(r'^[a-zA-Z_ ]*$', "This field should only contain letters.")
nums = RegexValidator(r'^[0-9]*$', "Phone number should only contain numbers.")

class Patient(models.Model):
    unique_id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=100, validators=[letters])
    last_name = models.CharField(max_length=100, validators=[letters])
    date_of_birth = models.DateField(validators=[validate_birthyear], help_text="YYYY-MM-DD")
    street = models.CharField(max_length=40, default="")
    city = models.CharField(max_length=20, validators=[letters])
    state = models.CharField(max_length=20, validators=[letters], null=True, blank=True)
    postcode = models.CharField(max_length=8)
    phone = models.CharField(max_length=10, validators=[nums])
    email = models.EmailField(max_length=50, null=True, blank=True)

    class Meta: 
        ordering = ['unique_id', 'first_name', 'last_name', 'date_of_birth', 'street', 'postcode', 'phone', 'email']

    def get_absolute_url(self): 
        """Returns the url to access a particular instance of Patient"""
        return reverse('patient-details', args=[str(self.primary_key)])

    def __str__(self): 
        return f'{self.unique_id}, {self.first_name} {self.last_name}, {self.date_of_birth}, {self.street}, {self.postcode}, {self.phone}, {self.email}'

