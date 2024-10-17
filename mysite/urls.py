
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('user/profile/', include('user_profile.urls')),
    path('blog/', include('blog.urls')),
    path('dashboard/', include('dashboards.urls')),
    
    
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
