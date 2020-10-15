from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('<int:id_>', views.hero_id, name="hero ID"),
	path('<str:name>', views.hero_name, name="hero name"),
]
