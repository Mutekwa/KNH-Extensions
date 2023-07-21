from django.db import models

# Create your models here.
class Data(models.Model):
    Department = models.CharField(max_length=100)
    Section = models.CharField(max_length=100)
    Extension = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Department