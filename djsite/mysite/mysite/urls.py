from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('canteen.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "SduFoodPoint's Administration Page"