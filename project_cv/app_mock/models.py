from django.db import models

# Create your models here.
from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name
