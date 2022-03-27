from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

def index(request):
    return HttpResponse("<h1>Index<h1>")

def add(request):
    """Renders a form used to register a new patient"""
    return HttpResponse("<h1>Add</h1>")

def fetch(request):
    """Renders patient data"""
    return HttpResponse("<h1>Fetch</h1>")