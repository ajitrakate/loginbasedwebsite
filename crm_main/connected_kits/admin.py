from django.contrib import admin
from .models import Kit, Button
# Register your models here.


class ButtonInline(admin.TabularInline):
    model = Button
    extra = 1




class KitAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User", {"fields": ["user"]}),
        ("Kit", {"fields": ["manufacturer_name", "user_name"]},)
    ]
    inlines = [ButtonInline]





admin.site.register(Kit, KitAdmin)

