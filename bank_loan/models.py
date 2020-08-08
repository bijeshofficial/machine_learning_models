from django.db import models

# Create your models here.
class Approval(models.Model):

    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female', 'Female'),
    )

    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    GRADUATE_CHOICES = (
        ('Graduate', 'Graduate'),
        ('Not_Graduate', 'Not_Graduate'),
    )

    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban'),
    )

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 15, choices = GENDER_CHOICES)
    married = models.CharField(max_length = 15, choices = MARRIED_CHOICES)
    dependents = models.IntegerField(default = 0)
    education = models.CharField(max_length = 15, choices = GRADUATE_CHOICES)
    self_employed = models.CharField(max_length = 15, choices = SELFEMPLOYED_CHOICES)
    applicant_income = models.IntegerField(default = 0)
    co_applicant_income = models.IntegerField(default = 0)
    loan_amount = models.IntegerField(default = 0)
    loan_term = models.IntegerField(default = 0)
    credit_history = models.IntegerField(default = 0)
    property_area = models.CharField(max_length = 15, choices = PROPERTY_CHOICES)


    def __str__(self):
        return self.first_name + ' ' + self.last_name