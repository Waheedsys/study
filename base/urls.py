from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginpage, name='login'), 
    path('logout/', views.logoutuser, name='logout'), 
    path('register/', views.registerpage, name='register'), 
    path('', views.home, name='home'), 
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userprofile, name='user-profile'),
    path('create-room/', views.createRoom, name="create-room"), 
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicspage, name="topics"),
    path('activity/', views.activitypage, name="activity"),

]
