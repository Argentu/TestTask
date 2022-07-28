from django.urls import path
from . import views

urlpatterns = [
    path('<str:lang>/', views.Menu_view.as_view()),
    path('', views.start)
]
