from django.shortcuts import render
from django.template.defaultfilters import slugify


def index(request):
    return render(request, "main/main_page.html")