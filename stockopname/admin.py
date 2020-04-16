from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = (
        'kategori','nama',
        'jumlah','satuan',
        'harga','user',
        'timestamp','total'
    )

    list_filter = (
        'kategori','nama'
    )

admin.site.register(Permintaan)