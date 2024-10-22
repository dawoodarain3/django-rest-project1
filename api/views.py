from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from rest_framework.decorators import action
# Create your views here.

class CreateSignup(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCRUD(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def all_data(self,request):
        alldata = User.objects.all()
        serializer = UserSerializer(alldata,many=True)
        return Response(serializer.data)
    
    @action(detail=True,methods=['PATCH'])
    def edit(self,request,pk=None):
        if self.request.user.user_type.lower() != 'student':
            instance = User.objects.get(pk=pk)
            serializer = UserSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated!'})
            return Response(serializer.errors)
        return Response({'msg':'User is Student!'})
    
    @action(detail=True, methods=['DELETE'])
    def delete(self,request,pk=None):
        if self.request.user.user_type.lower() == 'doo':
            datadelete = User.objects.get(pk=pk)
            datadelete.delete()
            return Response({'msg':'Data Deleted!'})
        return Response({'msg':'User Must be DOO!'})