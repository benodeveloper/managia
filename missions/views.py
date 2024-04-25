import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from managia.helpers import parse_form_lists
from missions.models import Beneficiary, Mission

# Create your views here.
def index(request):
    missions = Mission.objects.all()
    return render(request, 'missions/index.html', {'missions': missions})

def create(request):
    form_data = parse_form_lists(request)
    
    beneficiary = Beneficiary.objects.create(
        first_name = form_data['beneficiary']['first_name'],
        last_name = form_data['beneficiary']['last_name'],
        phone_number = form_data['beneficiary']['phone_number'])
    
    Mission.objects.create(
        reference = form_data['reference'],
        order_number = form_data['order_number'], 
        date = datetime.datetime.strptime(form_data['date'], '%Y-%m-%d'), 
        status = "WAITING",
        beneficiary = beneficiary)
    return redirect('missions.index')


