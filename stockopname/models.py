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
    per_unit = models.IntegerField()
    satuan = models.IntegerField(choices=SATUAN)
    harga = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def status(self):
        if self.jumlah <= 0:
            status = 'Y'
        else:
            status = 'N'
        return '{}'.format(status)
    
    def total_unit(self):

        return '{}'.format(self.jumlah*self.per_unit)

    def total(self):
        
        return '{}'.format(self.jumlah*self.harga)
    
    def __str__(self):
        return '{}'.format(self.nama)
    

class Permintaan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    # sisa = models.IntegerField(default=0)
    tgl = models.DateTimeField(auto_now_add=True)

    def sisa(self):

        self.sisa = 0

        if self.sisa:

            self.sisa = Produk.total_unit - self.jumlah
        else:
            return '{}'.format(Produk.jumlah)
    
    def HargaSisa(self):
        unit = Produk.harga/Produk.per_unit
        self.HargaSisa = self.sisa * unit
        return '{}'.format(self.HargaSisa)