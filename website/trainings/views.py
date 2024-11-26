from django.shortcuts import render, get_object_or_404, redirect

from .admin import CategoryAdmin
from .models import Category, Training
from .forms import TrainingForm
from django.db import models


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'trainings/category_list.html', {'categories': categories})


def training_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    sort_order = request.GET.get('sort', 'asc')

    if sort_order == 'desc':
        trainings = Training.objects.filter(category_id=category).order_by('-price')
    elif sort_order == 'asc':
        trainings = Training.objects.filter(category_id=category).order_by('price')
    else:
        trainings = Training.objects.filter(category_id=category).order_by('date')


    return render(request, 'trainings/training_list_by_category.html',
                  {'category': category, 'trainings': trainings})


def training_detail(request, category_slug, training_id):
    category = get_object_or_404(Category, slug=category_slug)
    trainings = get_object_or_404(Training, training_id=training_id, category_id=category)
    return render(request, 'trainings/training_detail.html',
                  {'category': category, 'trainings': trainings})


def create_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новую тренировку в базу данных
            return redirect('training_list_by_category_page',
                            category_slug=form.cleaned_data['category'].slug)
    else:
        form = TrainingForm()
    return render(request, 'trainings/create_training.html', {'form': form})


def delete_training(request, training_id):
    training = get_object_or_404(Training, training_id=training_id)

    if request.method == 'POST':
        training.delete()
        return redirect('main_page')


def edit_training(request, training_id):
    training = get_object_or_404(Training, training_id=training_id)

    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('profile_page', id=training.trainer_id)
    else:
        form = TrainingForm(instance=training)
    return render(request, 'trainings/edit_training.html', {'form': form, 'training': training})
