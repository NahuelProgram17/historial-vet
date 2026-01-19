from django.contrib import admin
from .models import ClinicalRecord

@admin.register(ClinicalRecord)
class ClinicalRecordAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'species', 'owner', 'created_at')

def __str__(self):
    return f"{self.pet_name} ({self.get_species_display()})"