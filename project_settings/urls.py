from django.urls import path
from .views import SiteSettingsView

urlpatterns = [
    path("api", SiteSettingsView.as_view(), name="site_settings"),
]
