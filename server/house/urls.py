from django.urls import path, include
from .views import HouseCreateView, HouseListView, HouseUpdateView


urlpatterns = [
    path('house/create/', HouseCreateView.as_view()),
    path('house/list/', HouseListView.as_view()),
    path('house/update/<int:pk>', HouseUpdateView.as_view()),

]