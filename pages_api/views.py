from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Page
from .serializers import PagesSerializer
from .pagination import CustomPageNumberPagination


class PagesApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        # offers = Page.objects.filter(show_in_main_menu=False)
        offers = Page.objects.all()
        paginator = CustomPageNumberPagination()
        paginated_offers = paginator.paginate_queryset(offers, request)
        serializer = PagesSerializer(paginated_offers, many=True)

        return paginator.get_paginated_response(serializer.data)

    def menuItems(self, request, *args, **kwargs):
        offers = Page.objects.filter(show_in_main_menu=False)
        paginator = CustomPageNumberPagination()
        paginated_offers = paginator.paginate_queryset(offers, request)
        serializer = PagesSerializer(paginated_offers, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self):
        pass
