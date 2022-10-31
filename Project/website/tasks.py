from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import GameRound
from django.utils import timezone 


@shared_task
def Create():
    one = GameRound.objects.last()
    rounds = int(one.week) + 1
    GameRound.objects.create(week = rounds, time_generated = one.time_ending)