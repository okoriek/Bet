from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import GameRound, LotteryRound
from django.utils import timezone 

# Celery for game
@shared_task
def Create():
    one = GameRound.objects.last()
    rounds = int(one.week) + 1
    GameRound.objects.create(week = rounds, time_generated = one.time_ending)

# Celery for lottery 
@shared_task
def CreateLottery():
    one = LotteryRound.objects.last()
    rounds = int(one.week) + 1
    LotteryRound.objects.create(week = rounds, time_generated = one.time_ending)