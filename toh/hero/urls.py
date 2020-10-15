from django.urls import path

from . import views

urlpatterns = [
  path('<int:id>/', views.id_view, name='id_view'),
  path('<str:name>/', views.name_view, name='name_view'),
  path('info/<int:id>/', views.hero_info, name='hero_info'),
  path('', views.hero_list),
]
