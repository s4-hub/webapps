from django.db import models

# Create your models here.

BIDANG = (
    (1,'Kepesertaan'),
    (2,'Pelayanan'),
    (3,'Keuangan'),
    (4,'Umum & SDM'),
    (5,'Wasrik'),
    (6,'IT'),
)

class Kendala(models.Model):
    tgl_kendala = models.DateField()
    bidang = models.IntegerField(choices=BIDANG)
    keterangan = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)