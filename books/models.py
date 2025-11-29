from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Titulo", null=False, blank=False
    )
    author = models.CharField(
        max_length=200, verbose_name="Autor", null=False, blank=False
    )
    category = models.CharField(
        max_length=200, verbose_name="Categoria", null=False, blank=False
    )
    description = models.TextField(
        verbose_name="Descripción breve", null=False, blank=False
    )
    publication_date = models.DateTimeField(auto_created=True, null=False, blank=False)
    image = models.ImageField(
        upload_to="books/",
        null=True,
        blank=True,
        verbose_name="Portada",
    )

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

        constraints = [models.UniqueConstraint(fields=["title"], name="unique_title")]

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="favorited_by"
    )

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book"], name="unique_user_book_favorite"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
