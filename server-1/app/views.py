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

    _pre = Predict( raw_data['ph'] , raw_data['Turbidity'] )

    save({
        "timestamp" : datetime.now(),
        "raw-data" : raw_data,
        "processed": {
            "Hardness"          : _pre[0],
            "Solids"            : _pre[1],
            "Chloramines"       : _pre[2],
            "Sulfate"           : _pre[3],
            "Conductivity"      : _pre[4],
            "Organic_carbon"    : _pre[5],
            "Trihalomethanes"   : _pre[6],
            "Turbidity"         : _pre[7],
            "Potability"        : _pre[8]
        }
    })

    return Response( raw_data, status=status.HTTP_201_CREATED )