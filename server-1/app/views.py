from django.http import QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])    
def hw(request):
    print('REQUEST RECEIVED')

    data = dict(QueryDict(request.body))
    print( data )
    print( 'pH:\t\t' , data['pH'] )
    print( 'Turbidity:\t' , data['Turbidity'] )
    print( 'Temperature:\t' , data['Temperature'] )

    # print( request.data['name'] )

    return Response( request.data, status=status.HTTP_201_CREATED )