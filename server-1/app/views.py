from datetime import datetime
from django.http import QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mongo_interface import save
from .ml_model import Predict

@api_view(['POST'])    
def hw(request):
    # print('REQUEST RECEIVED')
    
    raw_data = dict(QueryDict(request.body))
    
    for key in raw_data:
        if ( type( raw_data[key] == list) ):
            raw_data[key] = raw_data[key][0]

        if ( type( raw_data[key] == str) ):
            raw_data[key] = float( raw_data[key] )

    Predict( raw_data['ph'] , raw_data['Turbidity'] )

    save({
        "timestamp" : datetime.now(),
        "raw-data" : raw_data,
        "processed": {
            "Hardness": 0,
            "Solids": 0,
            "Chloramines": 0,
            "Sulfate": 0,
            "Conductivity": 0,
            "Organic_carbon": 0,
            "Trihalomethanes": 0,
            "Turbidity": 0,
            "Potability" : 0
        }
    })

    return Response( raw_data, status=status.HTTP_201_CREATED )