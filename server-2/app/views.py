from django.shortcuts import render
from django.http import JsonResponse, QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import DataFetch

def dashboard(request):
    return render(request, "dashboard.html")

def api_dashboard(request):

    if request.method == "GET":
        data = DataFetch.DashboardData()
        return JsonResponse(data)