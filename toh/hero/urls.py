from django.urls import path

from . import views

urlpatterns = [
#        path('', views.index, name='index'),
#        path('<str:name>/', views.hero_name, name='hero_name'),
#        path('<int:id>/',views.hero_id),
        path('', views.hero_list),
        path('info/<int:id>/', views.hero_info),
]
