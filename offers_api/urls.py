from django.urls import path, include
from .views import OffersListApiView

urlpatterns = [
    path('offers/', OffersListApiView.as_view(), name='offers_list')
]
