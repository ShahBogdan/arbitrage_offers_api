from django.urls import path
from .views import PagesApiView, PageApiView

urlpatterns = [
    path('api', PagesApiView.as_view(), name='offers_list'),
    path('api/<int:page_id>/', PageApiView.as_view()),
]
