from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detalles/<int:book_id>/", views.book_detail, name="details"),
]
