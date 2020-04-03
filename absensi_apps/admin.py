from django.contrib import admin
from .models import Scan_Absen, Nik
# Register your models here.

@admin.register(Nik)
class NikAdmin(admin.ModelAdmin):
    list_display = ('user','nik')

@admin.register(Scan_Absen)
class AbsenAdmin(admin.ModelAdmin):
    list_display = ('nik','pilihan','jam')