from django.urls import path
from .views import PagesApiView

urlpatterns = [
    path('api', PagesApiView.as_view(), name='offers_list')
]
