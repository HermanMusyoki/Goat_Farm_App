from django.db import models

class Goat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    weight = models.FloatField()
    health_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
