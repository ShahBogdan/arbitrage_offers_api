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

    def post(self):
        pass


class PageApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, page_slug):
        try:
            return Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return None

    def get(self, request, page_slug, *args, **kwargs):
        page = self.get_object(page_slug)

        if not page:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PagesSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass


class MainMenuPagesApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        main_menu_pages = Page.objects.filter(show_in_main_menu=True)
        serializer = PagesSerializer(main_menu_pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass
