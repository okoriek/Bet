import site
from django.contrib import admin
from .models import *

admin.site.register(PremierLeagueTable)
admin.site.register(PremierLeagueFixture)
admin.site.register(PremierLeagueWeek)
admin.site.register(BetAccumulate)
