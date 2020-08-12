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
    # permission_classes = [permissions.IsAuthenticated]


def bank_approval(request):
    form  = ApprovalForm(None or request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        gender = form.cleaned_data['gender']
        married = form.cleaned_data['married']
        dependents = form.cleaned_data['dependents']
        education = form.cleaned_data['education']
        self_employed = form.cleaned_data['self_employed']
        applicant_income = form.cleaned_data['application_income']
        co_applicant_income = form.cleaned_data['co_applicant_income']
        loan_amount = form.cleaned_data['loan_amount']
        loan_term = form.cleaned_data['loan_term']
        credit_history = form.cleaned_data['credit_history']
        property_area = form.cleaned_data['property_area']
        

        print(firstname)

    context = {
        'form' : form,
    }

    return render (request, 'bank_loan/bank_loan.html', context)
    