from django.shortcuts import render
from django.contrib import messages
from .models import Patient
from .forms import AddPatientForm, GetPatientForm

def index(request):
    context = { 'patients': Patient.objects.all() }
    return render(request, 'commoninfo/index.html', context)

def add(request):
    """Renders a form used to register a new patient"""
    form = AddPatientForm()
    if request.method == "POST":
        form = AddPatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient has been successfully added.")
            
            form = AddPatientForm()  # Clears form
    context = { 'form': form }
    return render(request, 'commoninfo/add.html', context)

def fetch(request):
    """Renders patient data"""
    return render(request, 'commoninfo/fetch.html', context)
