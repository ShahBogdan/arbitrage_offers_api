from django.urls import path
from .views import PagesApiView, PageApiView, MainMenuPagesApiView

urlpatterns = [
    path('api', PagesApiView.as_view(), name='offers_list'),
    path('api/<str:page_slug>/', PageApiView.as_view()),
    path('api/main_menu_pages', MainMenuPagesApiView.as_view()),
]
