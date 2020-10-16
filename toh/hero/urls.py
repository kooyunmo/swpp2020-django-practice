from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info),
    path('<int:id>/', views.hero_id, name='id'),
    path('<slug:name>/', views.hero_name, name='id')
]