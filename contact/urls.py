from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin',views.admin,name = 'admin'),

    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('add_video',views.add_video,name='add_video'),
    path('add_contact',views.add_contact,name='add_contact'),
]