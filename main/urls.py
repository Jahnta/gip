"""gip URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_layout', views.index2, name='home2'),
    path('chart/', views.chart, name='chart'),
    path('stations/', views.stations, name='stations'),
    path('<int:station_id>/station_detail/', views.station_detail, name='station_detail'),
    path('<int:unit_id>/unit_detail/', views.unit_detail, name='unit_detail'),
    path('<int:event_id>/event_detail/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('create_card/', views.create_card, name='create_card'),
    path('accounts/', include('django.contrib.auth.urls')),
]
