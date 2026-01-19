from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class ClinicalRecord(models.Model):

    SPECIES_CHOICES = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('caballo', 'Caballo'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    clinical_history = RichTextField()
    image = models.ImageField(upload_to='pets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet_name} ({self.species})"
