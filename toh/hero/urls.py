from django.urls import path

from . import views

"""
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.hero_name_id, name='hero_name_id'),
    path('<str:name>/', views.hero_name, name='hero_name'),   
]
"""

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info),
]