from django.contrib import admin
from django.urls import path, include  # Use path instead of url
from django.conf import settings
from django.conf.urls.static import static
from authenticate.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('home.urls')),  # Home page URL is handled by 'home.urls'
    path('', include('home.urls')),  # Home page (default)
    path('about/', include('about.urls')),  # About page URL
    path('contact/', include('contact.urls')),  # Contact page URL
    path('gallary/', include('gallary.urls')),  # Gallery page URL
    path('login/', login_view, name='login'),  # Login page URL
    path('logout/', logout_view, name='logout'),  # Logout page URL
    path('afterlogin/', include('authenticate.urls')),  # After login paths
    path('credentials/', include('authenticate.urls2')),  # Credentials path
    path('progress/', include('authenticate.urls3')),  # Progress path
    path('liveprogress/', include('authenticate.urls4')),  # Live progress path
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
