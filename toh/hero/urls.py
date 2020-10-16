from django.urls import path

from . import views
urlpatterns = [
    path('', views.hero_list),
    #path('', views.index, name='index'),
    path('<str:name>', views.hero_name, name='name'),
    path('<int:id>', views.hero_id, name='id'),
    path('info/<int:id>', views.hero_info, name='info'),
]