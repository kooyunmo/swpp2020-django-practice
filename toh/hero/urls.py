from django.urls import path
from . import views

urlpatterns = [
  path('', views.hero_list),
  path('', views.index, name='index'),
  path('<int:id>', views.hero_id, name='hero_id'),
  path('info/<int:id>', views.hero_info, name='hero_info'),
  path('<str:name>', views.hero_name, name='hero_name')
]