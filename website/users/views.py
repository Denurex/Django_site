from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from trainings.models import Training
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User
from bookings.models import Booking

from main import views as mainViews


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main_page")
            else:
                messages.error(request, "Неверные логин или пароль")
    else:
        form = LoginForm()

    return render(request, "users/signin.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main_page")


def check_profile(request, id):
    user = get_object_or_404(User, id=id)
    bookings = Booking.objects.filter(user_id=id)
    if user.is_trainer:
        trainings = Training.objects.filter(trainer_id=user.id)
        return render(
            request, "users/profile.html", {"user": user, "trainings": trainings}
        )
    else:
        if bookings is not None:
            # trainings = Training.objects.filter(training_id=bookings.training_id)
            return render(
                request, "users/profile.html", {"user": user, "bookings": bookings}
            )
        else:
            return render(request, "users/profile.html", {"user": user})
