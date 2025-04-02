from django.contrib import admin
from django.urls import path
from LostFound import views  # Import your views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
    path('submitfound/', views.submit_found_item, name='submit-found-item'),
    path("report_lost/", views.report_lost_item, name="report_lost"),
    path('listfound/', views.listfound, name='listfound'),
    path('listlost/', views.listlost, name='listlost'),  
    path('delete-found/<int:item_id>/', views.delete_found_item, name='delete_found_item'),
    path('delete-lost/<int:item_id>/', views.delete_lost_item, name='delete_lost_item'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
