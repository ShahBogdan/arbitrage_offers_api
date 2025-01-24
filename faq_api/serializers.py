from rest_framework import serializers
from .models import Faq


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            'id',
            "updated_at",
            "created_at",
            "question",
            "answer",
            "show_in_main"
        ]
