from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"users", views.UserViewset)
router.register(r"rides", views.RideViewset)
router.register(r"ride_events", views.RideEventViewset)

urlpatterns = [
    path("", include(router.urls))
]
