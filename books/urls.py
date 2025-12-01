from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detalles/<int:book_id>/", views.book_detail, name="details"),
    path(
        "agregar-favorito/<int:book_id>/favorito/",
        views.toggle_favorite,
        name="toggle_favorite",
    ),
    path(
        "mis-libros-favoritos", views.favorites_books_view, name="favorites_books_view"
    ),
]
