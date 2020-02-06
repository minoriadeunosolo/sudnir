from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CtClient
from .permissions import IsOwner
from .serializers import CtClientSerializer


class CtClientViewSet(viewsets.ModelViewSet):
    # A simple view to allow all CRUD operations
    queryset = CtClient.objects.all()
    serializer_class = CtClientSerializer
    permission_classes = [IsAuthenticated, IsOwner]
