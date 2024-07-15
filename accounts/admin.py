from django.contrib import admin
from .models import CustomeUser
from django.contrib.auth.admin import UserAdmin


class CustomeUserAdmin(UserAdmin):
    list_display = ("email", "is_staff", "is_active", "is_superuser", "is_verified")
    list_filter = ("is_verified",)
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ("Basic data", {"fields": ("email", "username", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomeUser, CustomeUserAdmin)
