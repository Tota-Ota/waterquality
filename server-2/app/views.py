from django.shortcuts import render
from django.http import JsonResponse, QueryDict

from .mongo_interface import fetch

def dashboard(request):
    return render(request, "dashboard.html")

def api_dashboard(request):
    if request.method == "GET":
        data = fetch()
        return JsonResponse(data)