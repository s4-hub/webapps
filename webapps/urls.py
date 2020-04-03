
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('')
    path('admin/', admin.site.urls),
    path('login/', views.signin, name='login'),
    path('kendala/', include('covid19_apps.urls', namespace='kendala')),
    path('absensi/', include('absensi_apps.urls', namespace='absensi')),
    path('', views.index, name='home'),
    path('logout/', views.singout, name='logout'),
]
