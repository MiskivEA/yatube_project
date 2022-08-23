from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    #home page
    path('', views.index, name = 'group_list'),
    #пока не знаю
    path('group_list/', views.group_list, name = 'group_list'),
    path('group/<slug:param>', views.group_posts, name = 'group_list')
]
