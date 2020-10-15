from django.urls import path
from . import views

urlpatterns = [
	path('', views.hero_list),
	path('info/<int:_id>/', views.hero_info),
	path('<str:_name>/', views.NAME),
]