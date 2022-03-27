from django import forms
from .models import Patient
import datetime

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['unique_id', 'first_name', 'last_name', 'date_of_birth', 'street', 'city', 'state', 'postcode', 'phone', 'email']
        labels = {'unique_id': "Patient ID", 'first_name': "First Name", 'last_name': "Last Name", 'date_of_birth': "Date of Birth", 'street': "Street", 'city': "City/Town", 'state': "State/Province/Region", 'postcode': "Postcode", 'phone': "Phone Number", 'email': "Email Address"}
        widgets = {'unique_id': forms.HiddenInput()}

    def validate_birthday(self):
        """Returns True if birthday is current date or in the past"""
        cleaned_data = super(AddPatientForm, self).clean()
        date_of_birth = cleaned_data.get('date_of_birth')

        if date_of_birth <= datetime.date.today():
            return True

        return False

class GetPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['unique_id']