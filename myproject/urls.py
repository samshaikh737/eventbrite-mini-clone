from django.contrib import admin
from django.urls import path

from app import views #Importing views from app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home")
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)