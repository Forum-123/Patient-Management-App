# Generated by Django 4.0.3 on 2022-04-04 20:57

import commoninfo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commoninfo', '0007_alter_patient_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(help_text='(YYYY-MM-DD)', validators=[commoninfo.models.validate_birthyear]),
        ),
    ]
