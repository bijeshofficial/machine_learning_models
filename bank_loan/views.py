from django.shortcuts import render
from django.core import serializers
from .models import Approval
from rest_framework import viewsets, permissions
from .serializers import approvalsSerializers
from .forms import ApprovalForm

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = approvalsSerializers
    permission_classes = [permissions.IsAuthenticated]


def bank_approval(request):
    form  = ApprovalForm()

    context = {
        'form' : form,
    }

    return render (request, 'bank_loan/bank_loan.html', context)