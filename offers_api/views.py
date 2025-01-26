from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Offer
from .serializers import OffersSerializer


class OffersListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        offers = Offer.objects.filter(show_offer=True)
        serializer = OffersSerializer(offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass
