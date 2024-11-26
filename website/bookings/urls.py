from django.urls import path
from . import views

urlpatterns = [
    path("booking-a-workout/<int:training_id>", views.booking_training, name="booking_workout_page"),
    path("cancel-a-workout/<int:booking_id>", views.cancel_booking, name="cancel_page"),
]
