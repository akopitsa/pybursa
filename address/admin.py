# -*- coding: utf-8 -*-
from django.contrib import admin
from address.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'obl', 'district', 'street')
    search_fields = ['country']
    list_filter = ['obl']
    ordering = ['country', 'street']


admin.site.register(Address, AddressAdmin)
