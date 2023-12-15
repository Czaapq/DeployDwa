
from django.urls import path
from DeployDwaWeb.views import wszystkie_bibiki, nowy_bibik, edytuj_bibika, usun_bibika

urlpatterns = [

    path('wszystkie/', wszystkie_bibiki, name="wszystkie_bibiki"),
    path('nowy/', nowy_bibik, name="nowy_bibik"),
    path('edytuj/<int:id>/', edytuj_bibika, name="edytuj_bibika"),
    path('usun/<int:id>/', usun_bibika, name="usun_bibika"),

]
