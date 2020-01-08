from django.shortcuts import render
from studentApp.models import student
from rest_framework.views import APIView
from studentApp.serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status

class studentView(APIView):
    def get_object(self):
        try:
            return student.objects.all()
        except:
            return status.HTTP_404_NOT_FOUND
            
    def get(self,request):
        queryset=self.get_object()
        serializer=studentSerializer(queryset,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=studentSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)




        



        


