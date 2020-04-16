from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PILIHAN = (
    (1,'Tersedia'),
    (2,'Kosong'),
)

KATEGORI = (
    (1,'CETAKAN'),
    (2,'ATK'),
    (3,'CONSUMABLE'),
)

SATUAN = (
    (1,'RIM'),
    (2,'BLK'),
    (3,'KBLK'),
    (4,'BKS'),
    (5,'BH'),
    (6,'KTK'),
    (7,'PAK'),
    (8,'PS'),

)

class Produk(models.Model):
    kategori = models.IntegerField(choices=KATEGORI)
    nama = models.CharField(max_length=50)
    jumlah = models.IntegerField()
    satuan = models.IntegerField(choices=SATUAN)
    harga = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def total(self):
        
        

        return '{}'.format(self.jumlah*self.harga)

class Permintaan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    tgl = models.DateTimeField(auto_now_add=True)

class SisaStok(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)

    def sisa(self):
        # self.sisa = Produk.jumlah - Permintaan.jumlah

        return '{}'.format(Produk.jumlah - Permintaan.jumlah)
    
    def HargaSisa(self):

        return '{}'.format(self.sisa * Produk.harga)
