from django.urls import path
from .views import OffersListApiView

urlpatterns = [
    path('api', OffersListApiView.as_view(), name='offers_list')
]
