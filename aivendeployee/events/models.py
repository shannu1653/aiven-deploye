from django.db import models
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title
