from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('accounts/login/', views.login, name='login'),
      path('buses/', views.buses, name='buses'),
     path('book/', views.book_seat, name='book_seat'),
     path('payment/<int:booking_id>/', views.payment, name='payment'),
     path('bookings/', views.bookings, name='bookings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
