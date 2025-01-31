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
            'main_page_og_image',
            'faq_page_title',
            'faq_page_h1',
            'faq_page_meta_desc',
            'faq_page_text',
            'faq_page_og_image',
            'pages_title',
            'pages_page_h1',
            'pages_meta_desc',
            'pages_og_image',
            'pages_text',
            'text_for_google_term',
            'footer_text',
            'show_pages',
            'ranking_page_title',
            'ranking_page_h1',
            'ranking_page_meta_desc',
            'ranking_page_og_image',
            'ranking_page_text',
            'logo_img',
            'site_policy'
        ]
