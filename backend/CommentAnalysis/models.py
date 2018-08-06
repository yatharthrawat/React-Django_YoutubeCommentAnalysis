from django.db import models

# Create your models here.

class Analysis (models.Model):
    Title = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        """ A string representation of the model"""
        result = "Title: "+ Title + "\n" + "url: " + url + "\n" + "Description: " + description + "\n"
        return result

