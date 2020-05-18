from django.db import models
from django.contrib.auth.models import User
# import datetime
# Create your models here.

PILIHAN = (
    (1,'JAM MASUK'),
    (2,'JAM PULANG'),
)

class Nik(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nik = models.CharField(max_length=9)

    def __str__(self):
        return '{}'.format(self.nik)
    

class Scan_Absen(models.Model):
    nik = models.ForeignKey(Nik, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pilihan = models.IntegerField(choices=PILIHAN)
    jam = models.DateTimeField(auto_now_add=True)

    