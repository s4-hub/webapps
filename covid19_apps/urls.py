from django.urls import path
from . import views

app_name='kendala'

urlpatterns = [
    # path('')
    path('daftar/', views.daftar, name='daftar'),
    path('', views.index, name='list'),
]
