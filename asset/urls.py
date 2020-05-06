from django.urls import path
from . import views

app_name = 'asset'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/new', views.create_category_view, name='new_category'),
    path('station/new', views.create_station_view, name='new_station'),
    path('asset/new', views.create_asset_view, name='new_asset')
]
