from site import venv
from django.urls import path

from .views import ProductListAPIView


urlpatterns = [
    path("", view=ProductListAPIView.as_view()),
]
