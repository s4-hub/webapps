from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = (
        'kategori','nama',
        'jumlah','satuan',
        'harga','user',
        'timestamp','status',
        'total_unit','total'
    )

    list_filter = (
        'kategori','nama'
    )

@admin.register(Permintaan)
class PermintaanAdmin(admin.ModelAdmin):
    list_display = (
        'produk','user',
        'jumlah','tgl',
        'sisa','HargaSisa',
    )
