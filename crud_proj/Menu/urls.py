from django.urls import path
from . import views


urlpatterns = [

    path ('', views.index,{'menu':'main_menu', 'title':'Main', 'headline':'Главная страница'}, name= 'home'),
    path('links/', views.index, {'menu':'main_menu', 'title':'Links', 'headline':'ССылки'}, name= 'links'),
    path('links/friends', views.index, {'menu':'main_menu', 'title':'Friends', 'headline':'Друзья'}, name= 'friends'),
    path('media/', views.index, {'menu':'main_menu', 'title':'Media', 'headline':'Медиа'}, name= 'media'),
    path('media/music', views.index, {'menu':'main_menu', 'title':'Music', 'headline':'Музыка'}, name= 'music'),
    path('media/music/rock', views.index, {'menu':'main_menu', 'title':'Rock', 'headline':'Рок'}, name= 'rock'),
    path('crypto/', views.index, {'menu':['main_menu', 'side_menu'], 'title':'Crypt', 'headline':'Крипта'}, name= 'crypto'),
    path('crypto/defi', views.index, {'menu':['main_menu', 'side_menu'], 'title':'DEFI', 'headline':'DEFI'}, name= 'defi'),
]
