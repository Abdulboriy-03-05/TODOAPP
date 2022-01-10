from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=400)
    text = models.TextField()
    color = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

