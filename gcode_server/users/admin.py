from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name',
                    'is_active', 'is_superuser',)
    list_filter = ('is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Персональная информация', {'fields': ('first_name',
                                                'last_name',
                                                'phone',
                                                )
                                     }),
        ('Данные', {'fields': ('last_login',
                               'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)
