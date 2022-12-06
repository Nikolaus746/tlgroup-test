from django.urls import path
from .views import Endpoint, IndexView, person_list

urlpatterns = [
    path('run/', Endpoint.as_view(), name="run"),
    path('', person_list, name="home"),

]
