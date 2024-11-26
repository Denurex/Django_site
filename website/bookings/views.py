from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Booking
from trainings.models import Training
from .forms import BookingForm
from django.utils import timezone
from django.db import transaction


def booking_training(request, training_id):

    if not request.user.is_authenticated:
        return HttpResponse(
            "Пожалуйста, зарегистрируйтесь или войдите, чтобы забронировать тренировку."
        )

    training = get_object_or_404(Training, training_id=training_id)

    if training.date < timezone.now():
        return HttpResponse("Эта тренировка уже прошла.")

    if request.method == "POST":
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            num_participants = form.cleaned_data["num_participants"]

            with transaction.atomic():
                training = Training.objects.select_for_update().get(training_id=training_id)

                if training.available_seats < num_participants:
                    return HttpResponse(f"Осталось только {training.available_seats} мест."
)

                Booking.objects.create(
                    user=request.user,
                    training=training,
                    num_participants=num_participants,
                    status="pending",
                )

                training.available_seats -= num_participants
                training.save()

            return redirect("main_page")
    else:
        form = BookingForm(user=request.user)

    return render(
        request, "bookings/booking_workout.html", {"form": form, "training": training}
    )


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)


    training = booking.training
    if booking.num_participants < training.available_seats:
        training.available_seats += booking.num_participants
    training.save()


    booking.status = "cancelled"
    booking.delete()

    return redirect("profile_page", booking.user.id)
