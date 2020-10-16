from django.urls import path

from . import views

urlpatterns = [
  path('', views.hero_list),
  path('info/<int:id>', views.hero_info, name="hero_info"),
  path('<int:id>', views.hero_name_by_id, name='hero_name'),
  path('<str:name>', views.hero_name_by_str, name='hero_name'),
]