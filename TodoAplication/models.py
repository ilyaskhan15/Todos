from django.db import models
from django.contrib.auth.models import User

class Todos(models.Model):
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    LOW = 'l'
    MEDIUM = 'm'
    HIGH = 'h'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    priority = models.CharField(max_length=1, default=HIGH, choices=PRIORITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def mark_completed(self):
        self.completed = True
        self.save()

# Create your models here.