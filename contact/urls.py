from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('admin_home',views.admin_home,name = 'admin_home'),

    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('add_video',views.add_video,name='add_video'),
    path('',views.add_contact,name='add_contact'),
    path('show_contact',views.show_contact,name='show_contact'),
    path('edit_contact/<pk>',views.edit_contact,name='edit_contact'),
    path('del_contact/<pk>',views.del_contact,name='del_contact'),
]