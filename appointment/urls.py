from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # create likr wifi
router.register('', views.AppointmentViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]