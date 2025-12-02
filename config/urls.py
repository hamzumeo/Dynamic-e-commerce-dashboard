from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Shop app routes
    path('', include('shop.urls')),

    # Django built-in auth URLs (login, logout, password change, reset)
    path('accounts/', include('django.contrib.auth.urls')),
]
