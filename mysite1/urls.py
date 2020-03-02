
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path('acceuil/', views.getgalerie),
    path('about/', views.about),
    path('detail/<int:id>', views.getdetail)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
