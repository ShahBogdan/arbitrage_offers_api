from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Faq
from .serializers import FaqSerializer


class FaqApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        faq = Faq.objects.all()
        serializer = FaqSerializer(faq, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass


class FaqForMainPage(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        faq = Faq.objects.filter(show_in_main=True)
        serializer = FaqSerializer(faq, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass
