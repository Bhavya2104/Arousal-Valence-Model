from django.urls import path, include
from . import views


urlpatterns = [
   path('<int:id>', views.home, name='home'),
   path('', views.game, name='game'),
   path('report', views.report, name='report'),
   path('erase', views.erase , name = "erase")
]