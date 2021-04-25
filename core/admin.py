from django.contrib import admin
from core.models import Apoiadores


@admin.register(Apoiadores)
class ApoiadoresAdmin(admin.ModelAdmin):
    pass
