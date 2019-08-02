from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name='index' ),
    path('register/', views.inscription),
    path('login/', views.connexion, name="connexion"),
    path('profile',views.profile ,name='profile'),
    path('myLogin',views.myLogin,name='mylog'),
    path('mylogout',views.mylogout,name='mylogout'),
    path('scrap',views.scrap,name='scrap'),
    path('resultat',views.resultat,name='resultat'),
]