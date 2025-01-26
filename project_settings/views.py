from django.shortcuts import render, redirect
from .models import SiteSettings
from .serializers import ProjectSettingsSerializers
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class SiteSettingsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        settings = SiteSettings.objects.first()
        serializer = ProjectSettingsSerializers(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass
