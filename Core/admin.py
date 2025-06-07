from django.contrib import admin
from .models import PasswordReset
from patient.models import Patient  # Correct if Patient is in patient app


admin.site.register(PasswordReset)
admin.site.register(Patient)
