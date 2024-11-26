from django import forms
from .models import Booking
from users.models import User


class BookingForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", disabled=True)
    last_name = forms.CharField(label="Фамилия", disabled=True)
    num_participants = forms.IntegerField(
        label="Количество участников",
        min_value=1,
        initial=1,
        help_text="Введите количество участников",
    )

    class Meta:
        model = Booking
        fields = [
            "first_name",
            "last_name",
            "num_participants",
        ]  # Добавляем поля в форму

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].initial = user.first_name
        self.fields["last_name"].initial = user.last_name
