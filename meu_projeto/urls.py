from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('sistema.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])