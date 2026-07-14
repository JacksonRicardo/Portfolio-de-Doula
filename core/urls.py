from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/download/", views.download_portfolio, name="download_portfolio"),
]
