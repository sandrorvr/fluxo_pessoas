from django.urls import path
from .views import fluxoList, fluxoUD

urlpatterns = [
    path('fluxo/',fluxoList.as_view(),name='fluxoT'),
    path('fluxo/total/<int:pk>/',fluxoList.as_view(),name='fluxoT'),
    path('fluxo/alter/<int:pk>/',fluxoUD.as_view(),name='fluxoUD'),
    
]