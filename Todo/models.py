from django.db import models
from django.contrib.auth.models import User


# ========== class-to-generate-task-table ==========

class Todolist(models.Model):
    unique_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    checked = models.BooleanField(default=False)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.tasktitle


# ========== class-to-generate-contact-table ==========

class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
