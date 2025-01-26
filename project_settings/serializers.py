from rest_framework import serializers
from .models import SiteSettings


class ProjectSettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            'site_name',
            'contact_email',
            'enable_feature',
            'main_page_h1',
            'main_page_title',
            'main_page_meta_desc',
            'main_page_text',
            'faq_page_title',
            'faq_page_h1',
            'faq_page_meta_desc',
            'faq_page_text',
            'pages_title',
            'pages_page_h1',
            'pages_meta_desc',
            'pages_text'
        ]
