from django.db import models

# Create your models here.
class Movie(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    release_on = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.TextField()
    rating = models.IntegerField()