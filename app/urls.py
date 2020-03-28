from . import views 
from django.urls import path
from netfile import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('join/', views.join, name="join"),
    path('logout/', views.logout_view, name="logout")
]


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)