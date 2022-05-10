from posixpath import basename
from django.urls import path, include
from statballerz import views
from django.contrib import admin

from rest_framework.routers import DefaultRouter
##from rest_framework.authtoken.views import obtain_auth_token

##from django.contrib.auth.models import User


router = DefaultRouter()
router.register(r'central', views.CentralViewSet, basename = "central")
##router.register(r'user', views.UserViewSet, basename="user")
router.register(r'players', views.PlayerViewSet, basename= "players")
router.register(r'playerleaderboard', views.PlayerLeaderBoardSet, basename= "playerleaderboard")
router.register(r'goalkeeper', views.GoalKeeperSet, basename = "goalkeeper")

urlpatterns = [
    
    path('', include(router.urls)),
    path('admin/', admin.site.urls,name="admin"),
    path('players/', views.PlayerViewSet.as_view(...)),
    # path('api/', include(router.urls)),
   ## path('api-token-auth/', obtain_auth_token, name='api-token-auth'),

    #path('', include('user.urls')),
    ##path('api-auth/', include('rest_framework.urls')),
    
    
]