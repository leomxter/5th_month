from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin #mixin - собирает все апишки в одну
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, AllowAny 
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render

from apps.cars.models import Car
from apps.cars.serializers import CarSerializer, SpecialMarks, SpecialMarksSerializer, PeriodsOwnership, PeriodsOwnershipSerializer

# Create your views here.
class StandardResultSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page size'
    max_page_size = 5
class CarAPIViewSet(GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['license_plate',]
    permission_classes = [AllowAny]
    pagination_class = StandardResultSetPagination

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (AllowAny(), )
        return (IsAdminUser(), )
        

class SpecialMarksAPIViewSet(GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    queryset = SpecialMarks.objects.all()   
    serializer_class = SpecialMarksSerializer

class PeriodsOwnershipAPIViewSet(GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    queryset = PeriodsOwnership.objects.all()
    serializer_class = PeriodsOwnershipSerializer 

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (AllowAny(), )
        return (IsAdminUser(), )

def home(request):
    context={
        'title' : 'Home'
    }
    return render(request, 'index.html')

def checked(request):
    return render(request, 'checked.html')