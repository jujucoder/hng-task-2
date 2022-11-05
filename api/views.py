from rest_framework.generics import GenericAPIView
from .serializers import InputSerializer
from rest_framework import status, response

# Create your views here.

KEYWORDS = ['add','subtract','multiply','addition','subtraction','multiplication','product','sum']

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
        operation_type_list = self.request.data['operation_type'].split()

        
        if (len(operation_type_list) == 1):
           if (operation_type ==  'addition' ):
            result = int(x) + int(y)
           elif (operation_type ==  'subtraction' ):
            result = int(x) - int(y)
           elif (operation_type ==  'multiplication' ):
            result = int(x) * int(y)
           else:
              return response.Response({ 'error':'invalid operation'}, status=status.HTTP_400_BAD_REQUEST, headers = header)     
           return response.Response({ "slackUsername": 'JayJayDev', 'operation_type':operation_type , 'result':result}, status=status.HTTP_200_OK, headers = header)  
        else :    
            
          

            if any((match := item)  in operation_type_list for item in KEYWORDS):
                operation = match
                
            

                if (operation ==  'add' or operation ==  'addition' or operation == 'sum'):
                    result = int(x) + int(y)
                    operation = 'addition'
                elif (operation ==  'subtract' or operation == 'subtraction' ):
                    result = int(x) - int(y)
                    operation = 'subtraction'
                elif (operation ==  'multiplication' or operation == 'multiply' or operation == 'product'):
                    result = int(x) * int(y)
                    operation= 'multiplication'
        
            

            return response.Response({ "slackUsername": 'JayJayDev', 'operation_type':operation , 'result':result}, status=status.HTTP_200_OK, headers = header)

