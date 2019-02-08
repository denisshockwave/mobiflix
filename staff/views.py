from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from content.myserializers import ContentSerializer
# Create your views here.c

class UploadContent(APIView):
    def post(self,request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def get(self,request):
        data=Content.objects.all()
        serializer = ContentSerializer(data,many=True)
        return Response(serializer.data)

class UploadContentDetailView(APIView):
    def get_object(self,id):
        try:
            return Content.objects.get(id=id)
        except Content.DoesNotExist:
            raise Http404

    def get(self,request,id):
        data=self.get_object(id)
        serializer = ContentSerializer(data,many=True)
        return Response(serializer.data)
    def put(self,request,id):
        #check if admin permission
        serializer = ContentSerializer(data=request.data,instance=self.get_object(id))
        return Response(serializer.data)
    def delete(self,request,id):
        #check if admin to delete
        status=self.get_object(id).delete()
        return Response({"status":status})

class ContentCategory(APIView):
    def post(self,request):
        serializer = ContentCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def get(self,request):
        data=Content.objects.all()
        serializer = ContentSerializer(data,many=True)
        return Response(serializer.data)

class ContentCategoryDetailView(APIView):
    def get_object(self,id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,id):
        data=self.get_object(id)
        serializer = ContentCategorySerializer(data,many=True)
        return Response(serializer.data)
    def put(self,request,id):
        #check if admin permission
        serializer = ContentCategorySerializer(data=request.data,instance=self.get_object(id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,id):
        #check if admin to delete
        status=self.get_object(id).delete()
        return Response({"status":status})
