"""
URL configuration for aircraft_production project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render, redirect
from django.urls import path

from aircraft_production import views
from aircraft_production.views import register_employee, login_employee, logout_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login'), name='root'),
    path('register/', register_employee, name='register'),
    path('login/', login_employee, name='login'),
    path('logout/', logout_employee, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('produce-part/', views.produce_part, name='produce_part'),
    path('parts/', views.part_list, name='part_list'),
    path('parts/delete/<int:part_id>/', views.delete_part, name='delete_part'),
    path('recycled-parts/', views.recycled_parts, name='recycled_parts'),
    path('recycled-parts/restore/<int:part_id>/', views.restore_part, name='restore_part'),
    path('parts/decrement/<int:part_id>/', views.decrement_part, name='decrement_part'),
    path('montaj/', views.montaj_page, name='montaj_page'),  # Montaj sayfası için URL
    path('montaj/produce-aircraft/', views.produce_aircraft, name='produce_aircraft'),
    path('produced-aircrafts/', views.produced_aircraft_list, name='produced_aircraft_list'),  # Üretilen uçak listesi

]
