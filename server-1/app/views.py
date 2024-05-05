from django.http import QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mongo_interface import save


@api_view(['POST'])    
def hw(request):
    print('REQUEST RECEIVED')

    # data = dict(QueryDict(request.body))
    data = request.data

    print( data )

    # print( 'pH:\t\t' , data['pH'] )
    # print( 'Turbidity:\t' , data['Turbidity'] )
    # print( 'Temperature:\t' , data['Temperature'] )

    # print( request.data['name'] )

    save({
        "raw-data" : data,
        "processed": {
            "value1" : 1,
            "value2" : 2,
            "value3" : 3,
            "value4" : 4
        }
    })

    return Response( request.data, status=status.HTTP_201_CREATED )