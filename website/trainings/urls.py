from django.urls import path
from . import views

urlpatterns = [

    path("", views.category_list, name="category_list_page"),
    path("creating_training/", views.create_training, name="create_training_page"),

    path("delete/<int:training_id>/",
         views.delete_training,
         name="delete_training_page"),

    path("edit/<int:training_id>/", views.edit_training, name="edit_training_page"),

    path("<slug:category_slug>/",
         views.training_list_by_category,
         name="training_list_by_category_page"),

    path("<slug:category_slug>/<int:training_id>/",
         views.training_detail,
         name="training_detail_page")
]

