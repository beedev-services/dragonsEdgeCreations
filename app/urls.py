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
    path('uc/', views.uc),
    path('theAdmin/login/', views.theAdminLogin),
    path('theAdmin/signup/', views.theAdminSignup),
    path('theAdmin/register/', views.theAdminRegister),
    path('theAdmin/event/create/', views.createEvent),
    path('theAdmin/format/create/', views.createFormat),
    path('theAdmin/language/create/', views.createLang),
    path('theAdmin/product/create/', views.createProd),
    path('theAdmin/products/', views.theAdminAllProds),
    path('theAdmin/events/', views.theAdminAllEvents),
    path('theAdmin/event/<int:event_id>/view/', views.theAdminViewEvent),
    path('theAdmin/product/<int:product_id>/view/', views.theAdminViewProd),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)