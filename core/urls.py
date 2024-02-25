"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from ctypes.wintypes import SERVICE_STATUS_HANDLE
from http.client import SERVICE_UNAVAILABLE
from msilib.schema import ServiceControl
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
# from home.views import Service
urlpatterns = [
    path('admin/', admin.site.urls),


    path('',index,name="index"),
    path('signup/',signup,name="signup"),
    path('signin/',signin,name="signin"),
    path('home/', home , name="home"),
    path('logout/',logout,name="logout"),
    path('contact/', contact ,name="contact"),
    path('about/', about ,name="about"),
    path('service/',service,name="service"),
    path('portfolio/', portfolio ,name="portfolio"),
    # path('service/',Service.as_view(),name="class"),
    path('add_to_cart/',add_to_cart,name="add_to_cart"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)