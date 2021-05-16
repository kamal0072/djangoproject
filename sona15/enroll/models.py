from django.db import models
from django.urls import reverse

# Create your models here.
class SchoolModel(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("SchoolModel", kwargs={"pk": self.pk})
    
    