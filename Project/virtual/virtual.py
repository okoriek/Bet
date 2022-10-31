import imp
from . models import PremierLeagueFixture, PremierLeagueWeek
import random

def confirmgoal(week):
    game =PremierLeagueFixture.objects.filter(wk = week)
    wks =  PremierLeagueWeek.objects.get(wk = week)
    result = []
    if wks.completed == False:
        start_game = 0
        while ( start_game < 3): 
            for i in game:
                chanceHome = random.randint(0, 20)
                chanceAway = random.randint(0, 20)
                if chanceHome < i.home.skills:
                    i.home_score += 1
                    i.save()
                else:
                    pass
                if chanceAway < i.away.skills:
                    i.away_score += 1
                    i.save()
                else:
                    pass
                item = {'home':str(i.home),'away':str(i.away), 'home_score': i.home_score, 'away_score': i.away_score}
                result.append(item)
            start_game += 1
        wks.completed = True
        wks.save()
        return result
        
    else:
        for i in game:
            item = {'home':str(i.home),'away':str(i.away), 'home_score': i.home_score, 'away_score': i.away_score}
            result.append(item)
        return result 