from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from log_app import views

router = DefaultRouter()
router.register(r'zones', views.ZoneViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'rates', views.RateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/rate-lookup/', views.RateLookupView.as_view(), name='rate-lookup'),
    path('api/lookup-city/', views.RateLookupByCityView.as_view(), name='lookup-city'),
]
