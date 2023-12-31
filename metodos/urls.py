from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('metodos/', views.metodos, name="metodos"),
    path('biseccion/', views.biseccion, name="biseccion"),
    path('reglafalsa/', views.reglafalsa, name="reglafalsa"),
    path('newtonRaphson/', views.newtonRaphson, name="newtonRaphson"),
    path('secante/', views.secante, name= "secante"),
    path('raicesMultiples/', views.raicesMultiples, name="raicesMultiples"),
    path('raicesMultiples2/', views.raicesMultiples2, name="raicesMultiples2"),
    path('PuntoFijo/', views.puntofijo, name = "PuntoFijo"),
    path('jacobiSeid/', views.jacobiSeid, name = "jacobiSeid"),
    path('sor/', views.SOR, name = "SOR"),
    path('vandermonde/', views.vandermonde, name = "vandermonde"),
    path('newton/', views.newton, name = "newton"),
    path('lagrange/', views.lagrange, name = "lagrange"),
    path('spline/', views.spline, name = "spline"),
    
]
