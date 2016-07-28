from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

