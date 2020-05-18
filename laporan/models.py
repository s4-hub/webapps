from django.db import models

KIND = (
    (0,'CORPORATE'),
    (2,'START UP'),
)

class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    kind = models.IntegerField(default=0, choices=KIND)

class Job(models.Model):
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=8, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)