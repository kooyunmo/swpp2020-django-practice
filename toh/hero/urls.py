from django.urls import path
from . import views

urlpatterns = [
    path('info/<int:id>/', views.hero_info),
    path('', views.hero_list),
    path('<int:id>/', views.id),
    path('<str:name>/', views.hero_name),
]