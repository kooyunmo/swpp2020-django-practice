from django.urls import path

from . import views

urlpatterns = [
	path('', views.hero_list),
	path('info/<int:id_>/', views.hero_view),
]
