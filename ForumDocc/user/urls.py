from django.urls import path
from . import views

app_name='user'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.user_profile, name='user_profile'),
    path('update/', views.update, name='update_profile'),
    path('update/done', views.update_completed, name='update_completed'),
    path('logout/', views.logout, name='logout'),
]
