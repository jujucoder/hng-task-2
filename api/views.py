from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import InputSerializer
from rest_framework import status, response

# Create your views here.


class SolveView(GenericAPIView):
    serializer_class = InputSerializer
    def post(self, request, *args, **kwargs):
        header = {
            "Access-Control-Allow-Origin":"*"
        }
       
        if (self.request.data['x'] == ''):
            return response.Response({'error':'missing field'}, status=status.HTTP_400_BAD_REQUEST, headers = header)
        elif(self.request.data['y'] == ''):
            return response.Response({'error':'missing field'}, status=status.HTTP_400_BAD_REQUEST, headers = header)   
        elif(self.request.data['operation_type'] == ''):
            return response.Response({'error':'missing field'}, status=status.HTTP_400_BAD_REQUEST, headers = header)    

        operation_type = self.request.data['operation_type']
        x=self.request.data['x']
        y=self.request.data['y']

        if (operation_type ==  'addition' ):
            result = float(x) + float(y)
        elif (operation_type ==  'subtraction' ):
            result = float(x) - float(y)
        elif (operation_type ==  'multiplication' ):
            result = float(x) * float(y)
        else:
           return response.Response({ 'error':'invalid operation'}, status=status.HTTP_400_BAD_REQUEST, headers = header)     
       
        

        return response.Response({ "slackUsername": 'JayJayDev', 'operation_type':operation_type, 'result':result}, status=status.HTTP_200_OK, headers = header)

