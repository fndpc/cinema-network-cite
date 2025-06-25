from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('movies/', include('movies.urls')),
    path('cinemas/', include('cinemas.urls')),
    path('about/', include('info.urls')),
    path('users/', include('users.urls')),
    path('showtimes/', include('showtimes.urls')),
    path('orders/', include('orders.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)