from django.urls import path
from torq import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('edit_pro/<int:id>', views.edit_pro, name='edit_pro'),
    path('view_pro/', views.view_pro, name='view_pro'),
    path('service/', views.service, name='service'),
    path('user_list/', views.user_list, name='user_list'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
