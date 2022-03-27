from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q

from .models import Patient
from .forms import AddPatientForm

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
    context = {}
    if request.method == "GET":
        try:
            patient = Patient.objects.filter(pk=list(request.GET.values())[0])
            context = { 'fetch': patient }
        except Exception as e:
            print(e)
    return render(request, 'commoninfo/fetch.html', context)
