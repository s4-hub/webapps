from django.db import models
from django.contrib.auth.models import User
import decimal

# Create your models here.

PROGRAM = (
    (1,'JKK & JKM'),
    (2,'JKK, JKM & JHT'),
)

BULAN_P = (
    (1,'1 Bulan'),
    (3,'3 Bulan'),
    (6,'6 Bulan'),
    (12,'1 Tahun'),
)

class data_tk(models.Model):
    nama = models.CharField(max_length=50)
    nik = models.CharField(max_length=16)
    tgl_lhr = models.DateField()
    tmp_lhr = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class pekerjaan_tk(models.Model):
    nama_tk = models.ForeignKey(data_tk, on_delete=models.CASCADE)
    pekerjaan = models.CharField(max_length=30)
    penghasilan = models.FloatField()

class program_winback(models.Model):
    program = models.IntegerField(choices=PROGRAM)
    bulan = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def iuran(self):

        if (self.program == 1):
            jkk = decimal.Decimal(pekerjaan_tk.penghasilan) * decimal.Decimal('0.01')
            jkm = 6800
            bln = self.bulan
            self.iuran = bln * (jkk + jkm)
            # return self.total
        else:
            jkk = decimal.Decimal(pekerjaan_tk.penghasilan) * decimal.Decimal('0.01')
            jht = decimal.Decimal(pekerjaan_tk.penghasilan) * decimal.Decimal('0.02')
            jkm = 6800
            bln = self.bulan
            self.iuran = self.bulan * (jkk + jht + jkm)
        return self.iuran


            