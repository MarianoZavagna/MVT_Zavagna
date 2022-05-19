"""Proyecto_MarianoZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Proyecto_MarianoZ.views import(
    post_family,
    get_family,
    all_family,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("post_family/<str:name>/<int:dni>", post_family),
    path("get_family/<int:id>", get_family),
    path("all_family/", all_family),

]
