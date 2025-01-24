from rest_framework import serializers
from .models import Page


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', "meta_title", "meta_description",
                  "image", 'h1', 'text', 'show_in_main_menu']
