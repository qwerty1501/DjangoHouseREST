from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/base-auth', include('rest_framework.urls')),
    path('api/v0/', include('house.urls')),
    path('api/v0/auth/', include('djoser.urls')),
    path('api/v0/auth-token', include('djoser.urls.authtoken')),

]
