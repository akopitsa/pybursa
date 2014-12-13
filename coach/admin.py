# -*- coding: utf-8 -*-
from django.contrib import admin
from coach.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'type', 'phone', 'email')
    search_fields = ['name']
    list_filter = ['type']
    ordering = ['type', 'name']
    radio_fields = {"type": admin.HORIZONTAL}

admin.site.register(Coach, CoachAdmin)

