from django.urls import path

urlspatter = [
    path(""),
    path("posts"),
    path("posts/<slug:slug>"),
]