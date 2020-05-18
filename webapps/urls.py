
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
# from decorator_include import decorator_include
from . import views
from absensi_apps import views as apps_views

urlpatterns = [
    # path('')
    path('admin/', admin.site.urls),
    path('daftar/', views.register, name='register'),
    path('login/', views.signin, name='login'),
    path('kendala/', include('covid19_apps.urls', namespace='kendala')),
    path('absensi/', include('absensi_apps.urls', namespace='absensi')),
    path('stockopname/', include('stockopname.urls', namespace='stockopname')),
    path('fontawesome/', views.fontawesome, name='fontawesome'),
    path('themify/', views.themify, name='themify'),
    # path('stockopname/', decorator_include(login_required, 'stockopname.urls', namespace='stockopname')),
    path('', apps_views.index, name='home'),
    path('logout/', views.singout, name='logout'),
]
