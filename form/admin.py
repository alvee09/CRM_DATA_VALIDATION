from django.contrib import admin

admin.site.site_header = "C&A Source Input Form"
admin.site.site_title = "C&A Source Input Form"
admin.site.index_title = "C&A Source Input Form"
# Register your models here.
from .models import shipment_details, supplier_details

admin.site.register(shipment_details)
admin.site.register(supplier_details)