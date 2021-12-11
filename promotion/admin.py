from django.contrib import admin
from .models import Promotion

admin.site.register(Promotion)


class PromotionAdmin(admin.ModelAdmin):
    """Promotion Admin Definition"""

    list_display = ("name_kor",)
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "symbol",
                    "party",
                    "name_kor",
                    "name_hanja",
                    "sex",
                    "birth",
                    "job",
                    "educational_background",
                    "career",
                    "bulletin",
                    "poster",
                    "pledge",
                ),
            },
        ),
    )
