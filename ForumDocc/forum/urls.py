from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='forum'
urlpatterns=[
    path('thread/<int:thread_id>/', views.thread, name='thread'),
    path('newthread/upload/', views.new_thread, name='new_thread'),
    path('thread/delete/<int:pk>/', views.delete_thread, name='delete_thread')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
