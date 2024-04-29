from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import DataFetch
# from . import DataSave

def dashboard(request):
    return render(request, "dashboard.html")

def api_dashboard(request):

    if request.method == "GET":
        data = DataFetch.DashboardData()
        return JsonResponse(data)

@api_view(['POST'])    
def hw(request):
    print( request.data )
    # print( request.data['name'] )

    return Response( request.data, status=status.HTTP_201_CREATED )