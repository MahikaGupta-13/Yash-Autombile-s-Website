from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ServiceBooking(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   bikeName = models.CharField(max_length=150)
   model_no = models.CharField(max_length=15)
   problem = models.TextField()
   time = models.TimeField()


class SendMessage(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   message = models.TextField()

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content

    
class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

