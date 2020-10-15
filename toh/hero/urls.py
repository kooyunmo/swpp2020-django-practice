from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:heroId>/', views.hero_info),
    path('<int:int>/', views.readInt, name='index'),
    path('<str:string>/', views.readStr, name='index'),
    # path('', views.index, name='index'),
]
