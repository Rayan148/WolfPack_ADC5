from django.urls import path
from . import views

app_name="api"

urlpatterns = [
	path('api/', views.read_api_data, name = 'read_api'),
	path('api/update/<int:pk>/', views.update_api_data, name = 'update_api'),
	path('api/create/', views.create_api, name = 'create_api'),
	path('api/delete/<int:pk>/', views.delete_api_data, name = 'delete_api_data'),
	path('api/pagination/<int:PAGENO>/<int:SIZE>/', views.api_pagination, name='threads_pagination'),
]
