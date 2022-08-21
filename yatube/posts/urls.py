from django.urls import path

from . import views

urlpatterns = [
    #home page
    path('', views.index),
    #пока не знаю
    path('group/<slug:param>', views.group_posts)
]
