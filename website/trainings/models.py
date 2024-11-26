from django.db import models
from users.models import User
from unidecode import unidecode
from django.template.defaultfilters import slugify, default


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Training(models.Model):
    training_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="trainings")
    description = (models.TextField())
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trainings")
    date = models.DateTimeField()
    duration = (models.PositiveIntegerField())  #
    price = models.DecimalField(max_digits=6, decimal_places=2)
    max_participants = (models.PositiveIntegerField())
    available_seats = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.available_seats:
            self.available_seats = self.max_participants
        super(Training, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.trainer_id.username}"
