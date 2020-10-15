from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list, name='list'),
    path('<int:id>', views.hero_id, name='id'),
    path('<str:name>', views.hero_name, name='name'),
    path('info/<int:id>', views.hero_info, name='info')
]
