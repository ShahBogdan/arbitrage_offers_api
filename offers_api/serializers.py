from rest_framework import serializers

from .models import Offer, Advantages, RepaymentMethods, Documents


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['id', 'text']


class RepaymentMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepaymentMethods
        fields = ['id', "text"]


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['id', "text"]


class OffersSerializer(serializers.ModelSerializer):
    advantages = AdvantagesSerializer(many=True, read_only=True)
    documents = DocumentsSerializer(many=True, read_only=True)
    repayment_methods = RepaymentMethodsSerializer(
        many=True, read_only=True)

    class Meta:
        model = Offer
        fields = [
            'id',
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
            "legal_entity",
            "recommended",
            "zero_first",
            "offer_advantage",
            "country",
            "calculate_template",
        ]
