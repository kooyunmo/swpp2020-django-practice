from django.urls import path

from . import views

urlpatterns = [
  path('', views.hero_list, name='index'),
  path('info/<int:hero_id>/', views.hero_info, name='info'),
  path('<int:id>/', views.hero_id, name='id'),
  path('<str:name>/', views.hero_name, name='name'),
]