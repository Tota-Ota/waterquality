from django.shortcuts import render
from django.http import JsonResponse, QueryDict

from . import DataFetch

def dashboard(request):
    return render(request, "dashboard.html")

def api_dashboard(request):

    if request.method == "GET":
        data = DataFetch.DashboardData()
        return JsonResponse(data)