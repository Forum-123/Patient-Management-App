## Patient Management Application

### Purpose

A patient management application made using Django, which checks if the patient is already registered at the hospital and if not, the patient can be registered.

### Usage

In the terminal, use the command `python manage.py runserver` to launch the website on port 8000.
- Go to the URL `http://localhost:8000/commoninfo` to view all patients and their details
- Go to the URL `http://localhost:8000/commoninfo/add` to register a patient
- Go to the URL `http://localhost:8000/commoninfo/fetch` to search for a patient by their Patient ID and view all their details
    - Once the details for a patient are showing, there is the functionality to delete the patient if they are no longer in the system
