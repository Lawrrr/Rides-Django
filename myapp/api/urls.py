from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"users", views.UserViewset, basename="users")
router.register(r"rides", views.RideViewset)
router.register(r"ride_events", views.RideEventViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="jwt_login"),
]
