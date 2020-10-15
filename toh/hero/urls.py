from django.urls import path

from . import views
urlpatterns=[
        path('', views.hero_list, name='index'),
        path('info/<int:targetid>/', views.hero_info),
        path('<int:id>', views.heroid, name='id'),
        path('<str:name>', views.heroname, name='name'),
        ]
