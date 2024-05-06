from django.http import QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

    return Response( raw_data, status=status.HTTP_201_CREATED )