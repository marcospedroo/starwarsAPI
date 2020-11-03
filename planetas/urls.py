from django.urls import path

from . import views

urlpatterns = [
    path('planetas/', views.PlanetaList.as_view(), name='planeta-list'),
    path('planetas/<int:pk>/',  views.PlanetaDetail.as_view(), name="planeta-detail"),
    path('planeta/<str:nome>/',  views.PlanetaDetailCustom.as_view(), name="planeta-detail-nome"),
]

