from django.urls import path, include

from .views import HomePageView, cookie_preferences

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cookie-settings/',cookie_preferences, name='cookie' )
]
