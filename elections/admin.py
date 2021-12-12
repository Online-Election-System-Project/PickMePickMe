from django.contrib import admin
from . import models


@admin.register(models.Election)
class ElectionAdmin(admin.ModelAdmin):
    """Election Admin Definition"""

    list_display = (
        "title",
        "register_period_begin",
        "register_period_end",
        "election_period_begin",
        "election_period_end",
        "election_type",
    )
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "title",
                    "register_period_begin",
                    "register_period_end",
                    "election_period_begin",
                    "election_period_end",
                    "election_type",
                ),
            },
        ),
    )
