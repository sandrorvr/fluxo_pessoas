from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import fluxoSerializers
from chart.models import fluxo
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404



class fluxoList(generics.ListCreateAPIView):
    queryset = fluxo.objects.all()
    serializer_class = fluxoSerializers

    def get_queryset(self):
        if self.kwargs.get('pk'):
            return self.queryset.filter(total_pes=self.kwargs.get('pk'))
        return self.queryset.all()

class fluxoUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = fluxo.objects.all()
    serializer_class = fluxoSerializers