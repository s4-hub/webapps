from django.urls import path, include
from .views import AppStok


app_name = 'stockopname'
urlpatterns = [
    path('', AppStok.index, name='list'),
    # path('ajax_calls/search/', AppStok.autocompleteModel, name='search'),
    path('permintaan/<int:pk>', AppStok.PermintaanProduk, name='permintaan'),
    path('permintaan/list/', AppStok.permintaan_list, name='permintaan_list'),
    path('input/', AppStok.InputProduk, name='input'),
    path('sisa/', AppStok.sisa_stok, name='sisa'),
]
