from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.title
