from django.shortcuts import render, redirect
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def register(request: HttpRequest) -> HttpResponse:
    """
    Register a new user.

    Handles GET requests by displaying the registration form, and
    POST requests by validating the submitted form, creating the user,
    logging them in, and redirecting to the home page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: A rendered template with the registration form
        or a redirect to the home page on successful registration.
    """

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registrado con éxito")
            login(request, user)
            return redirect("home")  # type: HttpResponseRedirect
    else:
        form = CustomUserCreationForm()

    context: dict[str, Any] = {
        "form": form,
    }
    return render(request, "user/register.html", context)
