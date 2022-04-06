from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q

from .models import Patient
from .forms import AddPatientForm

def index(request):
    """Renders all patients' data in database"""
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
    """Renders one patient's data"""
    context = {}
    if request.method == "GET":
        try:
            patient = Patient.objects.filter(pk=list(request.GET.values())[0])
            context = { 'fetch': patient }
        except Exception as e:
            print(e)
    elif request.method == "POST":
        patient_to_delete = request.POST.get("deleteId")
        Patient.objects.filter(pk__in=patient_to_delete).delete()
        messages.success(request, "Patient has been successfully deleted.")
    return render(request, 'commoninfo/fetch.html', context)
