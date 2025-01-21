from rest_framework import serializers
from .models import Offer


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            "order",
            "updated_at",
            "created_at",
            "name",
            "offer_url",
            "image",
            "first_amount",
            "second_amount",
            "amount_from",
            "percent_per_day",
            "term_from",
            "term_to",
            "real_annual_rate_from",
            "real_annual_rate_to",
            "advantages",
            "repayment_methods",
            "documents",
            "age",
            "cash",
            "time_to_get",
            "on_lending",
            "bank_card",
            "bankID",
            "around_the_clock",
            "basic_characteristics_href",
            "user_warning",
            "license",
            "email",
            "address",
            "phone",
            "legal_entity"
        ]
