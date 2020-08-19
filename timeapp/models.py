from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    distance = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    average_speed = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def average_speed(self):
        if self.time > 0:
            #needed the float() to cast it out of an int
            return float(self.distance) / float(self.time)
        else:
            return 0

# class Report(models.Model):
#     average_speed = models.FloatField(default=0.0)
#     distance = models.IntegerField(default=0)
#     jogger = models.CharField(max_length=100)
#     #jogger = models.ForeignKey(Post, on_delete=models.CASCADE)
#     date = models.DateField(default=date.today)
#
#     def __str__(self):
#         return str(self.date)+" "+str(self.jogger)+" Distance: "+str(self.distance)+" "+ "Average Speed: "+str(self.average_speed)