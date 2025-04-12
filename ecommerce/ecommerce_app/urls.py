
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('',views.base,name="base"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
