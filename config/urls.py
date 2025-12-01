from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # main app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout/password reset
]
