"""local URL binding of the application"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="main_page"),
    path("test/", views.tst, name="test_page"),
    # path('info', views.about, name='info_page'),
    # path("product", views.shop, name="products_page"),
    # path("product/<int:id>/", views.product_detail, name="product_detail"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
