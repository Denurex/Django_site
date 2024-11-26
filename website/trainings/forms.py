from django import forms
from .models import Training
from users.models import User
from trainings.models import Category


class TrainingForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(
        queryset=User.objects.filter(is_trainer=True),
        widget=forms.Select,  # Виджет выбора
        label="Тренер",
        empty_label="",
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select,
        label="Категория",
        empty_label="",
    )

    class Meta:
        model = Training
        fields = [
            "title",
            "category",
            "description",
            "trainer",
            "date",
            "duration",
            "price",
            "max_participants",
        ]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)
        self.fields["trainer"].label_from_instance = (
            lambda obj: f" {obj.last_name} {obj.first_name}"
        )
