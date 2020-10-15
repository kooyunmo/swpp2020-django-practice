from django.urls import path

from . import views

urlpatterns = [
    path('',views.hero_list),
    path('info/<int:id>',views.hero_info ),
    path('<int:number>',views.showUrlNumber),
    path('<str:text>', views.showUrlText)
]