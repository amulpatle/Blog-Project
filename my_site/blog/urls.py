from django.urls import path

urlspatter = [
    path(""),
    path("posts"),
    path("posts/<slug:slug>"),#/posts/my-first-post
]