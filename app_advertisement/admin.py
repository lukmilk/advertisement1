from django.contrib import admin

# Register your models here.
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "created_date","updated_date", "auction", "show_photo"]
    list_filter = ["created_at", "auction"]
    actions = ["make_auction_as_false", "make_auction_as_true"]
    fieldsets = (
        (
            "Общее",{
                "fields": ("title", "description","user", "image"),
            }

        ),
        (
            "Финансы",{
                "fields":("price","auction"),
                "classes":["collapse"],
            }
        ),
    )

    @admin.display(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.display(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)