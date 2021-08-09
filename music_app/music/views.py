from django.http.response import Http404
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from music_app.music import serializers 

# Create your views here.

class Songlist(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk):
        song_id = self.get_object(pk)
        serializer = SongSerializer(song_id)
        return Response(serializer.data)

    def delete(self,request,pk):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class SongDetail(APIView):
    
    def get_object(self, pk):
        try:
          return Songlist.objects.get(pk=pk)
        except Songlist.DoesNotExist:
           raise Http404      

    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.update(song, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)