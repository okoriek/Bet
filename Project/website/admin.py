from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Custom, AccountAdmin)


@admin.register(Game)
class CustomGame(admin.ModelAdmin):
    list_display = ('week','user','generatedresult','selectednumber', 'winning', 'status')
    search_fields = ('user',)
    list_filter = ('status',)

@admin.register(CallRequest)
class CustomCall(admin.ModelAdmin):
    list_display = ('name','mobile_number','attended_to')
    search_fields = ('name','mobile_number')
    list_filter = ('attended_to','date_created',)

@admin.register(Commission)
class CustomCommission(admin.ModelAdmin):
    list_display = ('user','reward','date_created', 'completed')
    search_fields = ('user',)
    list_filter = ('date_created',)
    

admin.site.register(Result)
admin.site.register(NumberedValue)
admin.site.register(GameRound)
admin.site.register(Ticket)
admin.site.register(LotteryRound)
admin.site.register(WithdrawalPayment)

