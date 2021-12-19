from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('books/', views.books),
    path('art/', views.art),
    path('services/', views.services),
    path('contact/', views.contact),
    path('theAdmin/', views.theAdmin),
    path('logout/', views.logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)