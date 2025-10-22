from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdmin
from api.models import User
from api.serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
