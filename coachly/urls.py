from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from register import views as view_reg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', view_reg.register),
    path('', include('django.contrib.auth.urls')),
    path('', include('course.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
