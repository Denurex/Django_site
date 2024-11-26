from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Booking
import logging

logger = logging.getLogger(__name__)


@shared_task
def clean_old_bookings():
    logging.info("Запуск задачи очистки старых бронирований.")
    threshold_date = timezone.now() - timedelta(days=10)

    old_bookings = Booking.objects.filter(created_at__lt=threshold_date)

    logger.info(f'Найдено {old_bookings.count()} старых бронирований для удаления.')

    deleted_count, _ = old_bookings.delete()

    print(f"Удалено {deleted_count} старых бронирований.")
