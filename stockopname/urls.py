from django.urls import path, include
from .views import AppStok

app_name = 'stockopname'
urlpatterns = [
    path('', AppStok.index, name='list'),
    path('permintaan/<int:pk>', AppStok.PermintaanProduk, name='permintaan'),
    path('input/', AppStok.InputProduk, name='input'),
    path('sisa/', AppStok.Stoksisa, name='sisa'),
]
