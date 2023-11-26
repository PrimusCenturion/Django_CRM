from django.urls import path, include

from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
]
