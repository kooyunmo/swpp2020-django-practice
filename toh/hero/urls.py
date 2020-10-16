from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list),
    path('<str:name>', views.hero_name),
    path('<int:id>', views.hero_id),
]