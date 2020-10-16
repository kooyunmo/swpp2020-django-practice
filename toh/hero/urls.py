from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.hero_list),
    path('<int:id>/', views.id),
    path('<str:name>/', views.name),
    path('info/<int:id>/', views.hero_info),
]