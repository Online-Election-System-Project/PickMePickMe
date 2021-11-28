from django.contrib import admin
from . import models


@admin.register(models.Candidate)
class CandidateAdmin(admin.ModelAdmin):
    """Candidate Admin Definition"""

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
