from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['complete']

    @staticmethod
    def set_task_order(user, task_id_list):
        for index, task_id in enumerate(task_id_list):
            task = Task.objects.get(id=task_id, user=user)
            task._order = index
            task.save()