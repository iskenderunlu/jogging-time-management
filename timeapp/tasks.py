from celery import shared_task
import glob
import os
import io
#from timeapp.models import Post, Report
from django.db.models.query import QuerySet

from django.utils import timezone

from celery.task.schedules import crontab
from celery.decorators import periodic_task

############

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)



# #@periodic_task(run_every=(crontab(minute='*/10080')), name="weekly report update", ignore_result=True)
# #@shared_task
# @periodic_task(run_every=(crontab(minute='*/1')), name="save_avgspeed_distance_to_models", ignore_result=True)
# def save_avgspeed_distance_to_models():
#     today = timezone.now().date()
#     #posts = Post.objects.filter(date=[today - timezone.timedelta(days=7), today])
#     ###
#     posts = Post.objects.all()
#     ###
#     print("type(posts):" + str(type(posts)))
#     posts = posts.filter(date__range=(today - timezone.timedelta(days=7), today))
#
#     for post in posts:
#         joggerr = post.author
#         datee = post.date
#         average_speedd = post.average_speed
#         distancee = post.distance
#         report = Report.objects.create(jogger=joggerr, date=datee, average_speed=average_speedd, distance=distancee)
#         print("report: " + str(report))
