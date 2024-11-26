from django.db import models
from django.conf import settings
from trainings.models import Training


class Booking(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    training = models.ForeignKey( Training, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    num_participants = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.user} for {self.training}"

    class Meta:
        unique_together = ("user","training",)
