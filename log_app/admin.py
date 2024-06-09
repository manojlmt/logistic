from django.contrib import admin
from .models import Zone, City, Rate

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone_name')
    search_fields = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zone')
    search_fields = ('name',)
    list_filter = ('zone',)

class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_zone', 'to_zone', 'display_value')
    search_fields = ('from_zone__name', 'to_zone__name')

    def display_value(self, obj):
        ZONES_VALUES = {
            'Z1': [100, 11, 125, 130, 150],
            'Z2': [120, 125, 140, 150, 175],
            'Z3': [135, 145, 150, 175, 220],
            'Z4': [150, 165, 180, 200, 250]
        }
        return ZONES_VALUES.get(obj.value, "Invalid value")

    display_value.short_description = 'Value'

admin.site.register(Zone, ZoneAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Rate, RateAdmin)
