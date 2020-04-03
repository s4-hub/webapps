from django.urls import path
from . import views

app_name = 'absensi'

urlpatterns = [
    # path('')
    path('absen/', views.Scan, name='absen'),
    # path('keluar/', views.keluar, name='keluar'),
    # path('kendala/', include('covid19_apps.urls', namespace='kendala')),
    path('', views.index, name='list'),
    # path('logout/', views.singout, name='logout'),
]
