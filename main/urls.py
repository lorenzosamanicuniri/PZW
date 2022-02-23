from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('SviPrinteri', views.SviPrinteri, name='SviPrinteri'),
    path('SvaPlastika', views.SvaPlastika, name='SvaPlastika'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('proizvod/<proizvodjac>/', ProizvodjacPlastikaList.as_view()),
    
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)