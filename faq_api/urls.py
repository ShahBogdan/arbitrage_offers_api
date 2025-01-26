from django.urls import path
from .views import FaqApiView, FaqForMainPage

urlpatterns = [
    path('api', FaqApiView.as_view(), name='faq_list'),
    path('api/main', FaqForMainPage.as_view(), name='faq_main_page_list')
]
