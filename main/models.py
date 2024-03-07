from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title