from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField(default='')  # New field for description


    def __str__(self):
        return self.title
