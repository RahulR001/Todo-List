from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todolist(models.Model):
    unique_user = models.ForeignKey(User,on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    checked = models.BooleanField(default=False)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.tasktitle
