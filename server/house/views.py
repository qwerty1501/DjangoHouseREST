from rest_framework import generics
from .serializers import *
from .models import House
from .permissions import *
from rest_framework.permissions import IsAuthenticated


class HouseCreateView(generics.CreateAPIView):
    serializer_class = HouseSerializer
    permission_classes = (IsAuthenticated,)


class HouseListView(generics.ListAPIView):
    serializer_class = HouseListSerializers
    queryset = House.objects.all()


class HouseUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
