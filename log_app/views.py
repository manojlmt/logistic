from rest_framework import viewsets
from .models import Zone, City, Rate
from .serializers import ZoneSerializer, CitySerializer, RateSerializer, KG_value_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class RateLookupView(APIView):
    def post(self, request, *args, **kwargs):
        from_zone_id = request.data.get('from_zone')
        to_zone_id = request.data.get('to_zone')

        if not from_zone_id or not to_zone_id:
            return Response({"error": "from_zone and to_zone are required parameters."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            from_zone = Zone.objects.get(id=from_zone_id)
            to_zone = Zone.objects.get(id=to_zone_id)
        except Zone.DoesNotExist:
            return Response({"error": "Zone not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            rate = Rate.objects.get(from_zone=from_zone, to_zone=to_zone)
        except Rate.DoesNotExist:
            return Response({"error": "Rate not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = KG_value_Serializer(rate)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RateLookupByCityView(APIView):
    def post(self, request, *args, **kwargs):
        city_name_1 = request.data.get('city_name_1')
        city_name_2 = request.data.get('city_name_2')

        if not city_name_1 or not city_name_2:
            return Response({"error": "Both city_name_1 and city_name_2 are required parameters."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            city_1 = City.objects.get(name=city_name_1)
            city_2 = City.objects.get(name=city_name_2)
        except City.DoesNotExist:
            return Response({"error": "City not found."}, status=status.HTTP_404_NOT_FOUND)

        from_zone = city_1.zone
        to_zone = city_2.zone

        try:
            rate = Rate.objects.get(from_zone=from_zone, to_zone=to_zone)
        except Rate.DoesNotExist:
            return Response({"error": "Rate not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = KG_value_Serializer(rate)
        return Response(serializer.data, status=status.HTTP_200_OK)