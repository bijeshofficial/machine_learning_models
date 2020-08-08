from django.shortcuts import render
from django.core import serializers
from .models import Approval
from rest_framework import viewsets
from .serializers import approvalsSerializers

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = approvalsSerializers