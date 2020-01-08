from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# request.user : username
# request.auth: authorization

# function based views
@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        return Response(data={"name":"Sharique"}, status=status.HTTP_200_OK)
    elif request.method=='POST':
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response("Sorry. Invalid request.")


class Message(APIView):
    def get(self,request):
        return Response(data="get class based view",status=status.HTTP_200_OK)
    
    def post(self,request):
        return Response(data="post class based view",status=status.HTTP_200_OK)



