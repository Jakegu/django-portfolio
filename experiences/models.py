from django.db import models

class Tech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    entity = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    description = models.TextField()
    period = models.CharField(max_length=50)
    technologies = models.ManyToManyField(Tech)

    def __str__(self):
        return f"{self.name} - ({self.year})"