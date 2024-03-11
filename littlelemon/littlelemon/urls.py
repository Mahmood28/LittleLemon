from django.contrib import admin
from django.urls import path, include
from restaurant.views import BookingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"tables", BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/booking/", include(router.urls)),
    path("restaurant/", include("restaurant.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
