from django.urls import path
from .views import all_cars
from .views import A_Car

urlpatterns = [
    # Currently only takes GET requests
    path('', all_cars.as_view(), name='all_cars'),
    path('<str:id>/', A_Car.as_view(), name='a_car')
]