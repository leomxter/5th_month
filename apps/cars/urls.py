from rest_framework import routers
from django.urls import path

from apps.cars.views import CarAPIViewSet, SpecialMarksAPIViewSet, PeriodsOwnershipAPIViewSet, home, checked

router = routers.DefaultRouter()
router.register('cars', CarAPIViewSet, 'api_cars')
router.register('special', SpecialMarksAPIViewSet, 'api_special_marks')
router.register('periods', PeriodsOwnershipAPIViewSet, 'api_periods_ownership')

urlpatterns = [
    path('', home, name='home-page'),
    path('checked/', checked, name='found-page')
]