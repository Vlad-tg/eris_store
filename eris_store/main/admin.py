from .models import *
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):

    list_display = ("title", "id")
    ordering = ("title", "id")
    fieldsets = (
        (None, {
            'fields': ("category",
                       "brand",
                       "title",
                       "slug",
                       "image",
                       "description",
                       "price",
                       "total_rating",)
        }),
        ('Product: Laptop', {
            'fields': ("by_series",
                       "operating_system",
                       "screen_size",
                       "resolution",
                       "graphics",
                       "processor",
                       "cpu_speed",
                       "cpu_core",
                       "ram",
                       "storage_drive_size",
                       "touch",
                       "battery_charge",)
        }),
        ('Product: Smartphone', {
            'fields': ("operating_system_smartphone",
                       "diagonal",
                       "resolution_smartphone",
                       "camera",
                       "type_screen",
                       "processor_smartphone",
                       "ram_smartphone",
                       "battery_charge_smartphone",
                       "sd",
                       "sd_volume_max",
                       )
        }),
        ('Product: Headphone', {
            'fields': ("color",
                       "fit_type",
                       "item_dimensions",
                       "item_weight",
                       "battery",
                       )
        }),
    )


class VideoLaptopAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    ordering = ("name", "id")


class CPULaptopAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    ordering = ("name", "id")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "laptop", "id", "user")


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(VideoLaptop, VideoLaptopAdmin)
admin.site.register(VideoSmartphone)
admin.site.register(CPUSmartphone)
admin.site.register(CPULaptop, CPULaptopAdmin)
admin.site.register(RAM)
admin.site.register(OperatingSystemSmartphone)
admin.site.register(OperatingSystemLaptop)
admin.site.register(BySeriesLaptop)
admin.site.register(Brand)
admin.site.register(Compare)
admin.site.register(CompareProduct)
admin.site.register(SaleProductLaptop)
admin.site.register(BlogComment)
admin.site.register(RatingStar)
admin.site.register(PromoCode)

