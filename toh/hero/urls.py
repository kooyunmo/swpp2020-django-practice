from django.urls import path

from . import views

urlpatterns = [
  path('', views.hero_list, name="list"),
  path('info/<int:id>', views.hero_info, name="info"),
  # path('', views.index, name='index'),
  path('<int:id>', views.id, name='id'),
  path('<name>', views.name, name='name'),
  
]