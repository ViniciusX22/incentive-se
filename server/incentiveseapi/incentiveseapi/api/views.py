from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IncentiveSerializer, RequestSerializer
from .models import Incentive, Request

# Create your views here.


class IncentiveViewSet(viewsets.ModelViewSet):
    serializer_class = IncentiveSerializer
    queryset = Incentive.objects.all()


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
