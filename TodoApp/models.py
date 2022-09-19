from django.db import models


# Create your models here.


class TaskList(models.Model):
    task_name = models.CharField(max_length=200)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=30)
