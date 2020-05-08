from django.urls import path
from . import views

app_name = 'logistics'
urlpatterns = [
    path('', views.index, name='index'),
    path('activity/new', views.create_activity_view, name='new_activity'),
    path('activity/select', views.select_activity_view, name='select_activity')
]
