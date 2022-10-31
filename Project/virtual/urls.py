from django.urls import path
from . import views
app_name = 'virtual'

urlpatterns = [
    path('league/', views.Premier, name='premier_league'),
    path('fixture/', views.Fixture, name='fixture'),
    path('submitbet/', views.SubmitBet, name='submitbet'),
    path('getvirtualresult/', views.GenerateVirtualResult, name='getvirtualresult'),
]