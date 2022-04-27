from . models import NumberedValue
def number(request):
    value = NumberedValue.objects.all()
    return {'value':value}
