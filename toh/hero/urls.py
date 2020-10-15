from django.urls import path

from . import views

#urlpatterns = [
#        path('', views.index, name='index'),
#        path('<int:id>/', views.hero_id, name='hero_id'),
#        path('<str:name>/', views.hero_name, name='hero_name'),
#        ]
#

urlpatterns = [
        path('', views.hero_list),
        path('info/<int:target_id>/', views.hero_info),
        ]
