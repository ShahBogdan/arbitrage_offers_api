from django.urls import path
from .views import FaqApiView

urlpatterns = [
    path('api', FaqApiView.as_view(), name='faq_list')
]
