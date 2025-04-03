from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('movies/', include('movies.urls')),
    path('cinemas/', include('cinemas.urls')),
    path('about/', include('info.urls')),
    path('authorisation/', include('authorisation.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)