
from email.policy import default
import random
from django.utils import timezone
from django.db import models
from website.models import Custom

class PremierLeagueWeek(models.Model):
    wk =  models.IntegerField(default = 0)
    start_time = models.DateTimeField(blank = True, null = True)
    end_time =  models.DateTimeField(blank = True, null = True)
    completed = models.BooleanField(default = False)

    class Meta:
        ordering = ('wk',)

    def __str__(self):
        return str(self.wk)

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + timezone.timedelta(minutes=3)
        super().save(*args, **kwargs)


class PremierLeagueTable(models.Model):
    name = models.CharField(max_length=20)
    name_acron = models.CharField(max_length = 3)
    win = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    skills = models.IntegerField()
    

    def __str__(self):
        return str(self.name_acron)

    def save(self, *args, **kwargs):


        super().save(*args, **kwargs)


class PremierLeagueFixture(models.Model):
    wk =  models.ForeignKey(PremierLeagueWeek, on_delete=models.CASCADE , related_name = 'wks')
    home = models.ForeignKey(PremierLeagueTable, on_delete=models.CASCADE)
    away =  models.ForeignKey(PremierLeagueTable, on_delete=models.CASCADE, related_name = 'away_team')
    home_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    away_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    draw_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    homedraw_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    home_away_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    awaydraw_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    gg_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    ng_odd = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    over_two = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    under_two = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    over_three = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    under_three = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    over_four = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    under_four = models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits = 3)
    home_score = models.IntegerField(default = 0,)
    away_score = models.IntegerField(default = 0)
    home_win =  models.BooleanField(default = False)
    away_win =  models.BooleanField(default = False)
    draw =  models.BooleanField(default = False)

    class Meta:
        ordering = ('pk',)
    

    def __str__(self):  
        return f"Week{self.wk}:   {self.home} vs {self.away}"


    def save(self, *args, **kwargs):
        #calculating the home and away odd
        if self.home.skills and self.away.skills >=11 or self.home.skills and self.away.skills <11:
            self.home_odd = random.uniform(2.00, 2.40)
            self.away_odd = random.uniform(2.00, 2.50)
        if self.home.skills >= 11:
            self.home_odd = random.uniform(1.30, 1.90)
        else:
            self.home_odd = random.uniform(2.20, 2.50)
        if self.away.skills >= 11:
            self.away_odd = random.uniform(1.70, 2.10)
        else:
            self.away_odd = random.uniform(2.30, 2.75)
        #calculating the draw
        if self.home.skills and self.away.skills >=11 or self.home.skills and self.away.skills <11:
            self.draw_odd = random.uniform(3.20, 3.85)
        else:
            self.draw_odd = random.uniform(3.70, 4.80)
        #calculating the over goals
        if self.home.skills and self.away.skills >=11 or self.home.skills and self.away.skills <11:
            self.over_two = random.uniform(1.18, 1.23)
            self.under_two = random.uniform(3.50, 4.50)
            self.over_three = random.uniform(1.75, 1.85)
            self.under_three = random.uniform(1.80, 2.05)
            self.over_four = random.uniform(3.80, 4.40)
            self.under_four = random.uniform(1.18, 1.30)
        else:
            self.over_two =  random.uniform(1.20, 1.35)
            self.under_two = random.uniform(3.50, 4.50)
            self.over_three = random.uniform(1.80, 1.90)
            self.under_three = random.uniform(1.80, 190)
            self.over_four = random.uniform(3.70, 4.30)
            self.under_four = random.uniform(1.18, 1.30)
        #calculating the double chances
        self.homedraw_odd = self.home_odd / 1.5
        self.awaydraw_odd =  self.away_odd / 1.5
        self.home_away_odd = self.draw_odd / 2.5
        #calculating the bts and nbts
        if self.home.skills and self.away.skills >=11 or self.home.skills and self.away.skills <11:
            self.gg_odd = random.uniform(1.50, 1.70)
            self.ng_odd = random.uniform(1.80, 2.00)
        else:
            self.gg_odd = random.uniform(1.75, 1.85)
            self.ng_odd = random.uniform(1.80, 1.90)



        super().save(*args, **kwargs)





class BetAccumulate(models.Model):
    user_id = models.ForeignKey(Custom, on_delete = models.CASCADE, blank=True, null=True)
    betid = models.CharField(max_length = 20) 
    home = models.CharField(max_length = 20)
    away = models.CharField(max_length = 20)
    option = models.CharField(max_length = 20)
    odd = models.FloatField()    
    date = models.DateTimeField(default = timezone.now)
    won = models.BooleanField(default = False)
    loss = models.BooleanField(default = False)
    pending = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.betid}: {self.home} vs {self.away}"






