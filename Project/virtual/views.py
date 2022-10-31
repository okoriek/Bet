from calendar import week
import random
from turtle import home
from django.shortcuts import render
from django.http import JsonResponse
from .models import PremierLeagueFixture, PremierLeagueWeek, BetAccumulate
from .utils import create_betid
from django.views.decorators.csrf import csrf_exempt
from .virtual import confirmgoal

def Premier(request):
    return render(request, 'games/virtual.html')


def Fixture(request):
    update_odd =  PremierLeagueFixture.objects.all()
    games = PremierLeagueFixture.objects.all().filter(wk=1)
    wks = PremierLeagueWeek.objects.get(wk = 1)
    for i in update_odd:
        i.save()
    data = []
    for i in games:
        item = {
            'home_team':str(i.home),
            'away_team':str(i.away),
            'home_odd':i.home_odd,
            'away_odd':i.away_odd,
            'draw_odd':i.draw_odd,
            'home_draw_odd':i.homedraw_odd,
            'away_draw_odd':i.awaydraw_odd,
            'home_away_win_odd':i.home_away_odd,
            'bts':i.gg_odd,
            'nbts':i.ng_odd,
            'over_two':i.over_two,
            'under_two':i.under_two,
            'over_three':i.over_three,
            'under_three':i.under_three,
            'over_four':i.over_four,
            'under_four':i.under_four
        }
        data.append(item)
    return JsonResponse({'data':data,'wk': wks.wk, 'time': str(wks.end_time)})


@csrf_exempt
def SubmitBet(request):
    user = request.user
    teams =  request.POST['fixtures']
    home = teams[0:3]
    away = teams[5:9]
    options = request.POST['option']
    odd = request.POST['odds']
    #Creating the bet id for all accumulator
    bet_id = request.POST['bet_id']
    #Creating the Bet accumulator for each bet
    bet = BetAccumulate.objects.create(user_id = user, betid = bet_id, home =home, away = away, option =options, odd =odd, pending = True)
    bet.save()

    return JsonResponse('submited successfully', safe=False)
    
def GenerateVirtualResult(request):
    # getting the week for which result will be display
    week = 1
    result = confirmgoal(week)
          
    return JsonResponse({'result': result})

    
