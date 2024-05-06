from datetime import datetime
from django.http import QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mongo_interface import save


@api_view(['POST'])    
def hw(request):
    print('REQUEST RECEIVED')
    
    raw_data = dict(QueryDict(request.body))
    
    for key in raw_data:
        if ( type( raw_data[key] == list) ):
            raw_data[key] = raw_data[key][0]

        if ( type( raw_data[key] == str) ):
            raw_data[key] = float( raw_data[key] )

    print( raw_data )

    """
    INSERT ML MODEL FEEDFORWARD NETWORK HERE 
    THEN INSERT THE FINAL COMPUTED VALUES BELOW 
    """

    save({
        "timestamp" : datetime.now(),
        "raw-data" : raw_data,
        "processed": {
            "value1" : 1,
            "value2" : 2,
            "value3" : 3,
            "value4" : 4
        }
    })

    return Response( raw_data, status=status.HTTP_201_CREATED )