from rest_framework import serializers
from .models import Zone, City, Rate

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'zone_name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'zone']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id', 'from_zone', 'to_zone', 'value']

ZONES_VALUES = {
    'Z1': [100, 11, 125, 130, 150],
    'Z2': [120, 125, 140, 150, 175],
    'Z3': [135, 145, 150, 175, 220],
    'Z4': [150, 165, 180, 200, 250]
}

class KG_value_Serializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        fields = ['id', 'from_zone', 'to_zone', 'value']

    def get_value(self, obj):
        return ZONES_VALUES.get(obj.value, "Invalid value")