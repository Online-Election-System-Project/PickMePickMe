from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "resident_registration_number",
                    "gender",
                    "main_city",
                    "sub_city",
                )
            },
        ),
    )

    list_display = (
        "resident_registration_number",
        "gender",
    )
