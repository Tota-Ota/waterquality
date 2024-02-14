from django.shortcuts import render
from django.http import JsonResponse

from . import DataFetch

def dashboard(request):
    return render(request, "dashboard.html")

def api_dashboard(request):

    if request.method == "GET":
        data = DataFetch.DashboardData()
        return JsonResponse(data)
    
    # if request.method == "POST":
    #     IP = request.POST['IP']
    #     SSHUsername = request.POST['SSHUsername']
    #     Password = request.POST['Password']

    #     Inventory.append(IP)
    #     Status[IP] = ['1', SSHUsername]

    #     return JsonResponse({'status': 'ok'})