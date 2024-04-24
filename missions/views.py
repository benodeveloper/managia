import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from missions.models import Mission

# Create your views here.
def index(request):
    missions = Mission.objects.all()
    return render(request, 'missions/index.html', {'missions': missions})

def create(request):
    reference = request.POST['reference']
    order_number = request.POST['order_number']
    mission = Mission.objects.create(reference= reference,order_number = order_number, date = datetime.date.today(), status= "WAITING")
    print(mission)
    return redirect('missions.index')


