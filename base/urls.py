from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('home/', include('pages.urls')),
]
