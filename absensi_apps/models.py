from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

PILIHAN = (
    (1,'JAM MASUK'),
    (2,'JAM PULANG'),
)

class Scan_Absen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pilihan = models.IntegerField(choices=PILIHAN)
    jam = models.DateTimeField(auto_now_add=True)
    # def flag_scan(self):
    #     if self.pilihan:
    #         self.flag_scan == 'Y'
    #     else:
    #         self.flag_scan == 'T'
    #     return self.flag_scan