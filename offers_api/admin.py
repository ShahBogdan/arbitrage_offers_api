from django.contrib import admin
from .models import Offer, Advantages, RepaymentMethods, Documents
from adminsortable2.admin import SortableAdminMixin


# admin.site.register(Offer)
admin.site.register(Advantages)
admin.site.register(RepaymentMethods)
admin.site.register(Documents)
# Register your models here.


@admin.register(Offer)
class OfferAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['order']
    list_display = ['order', 'name']
