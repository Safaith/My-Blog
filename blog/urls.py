from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingPage.as_view(), name="index"),
    path("posts", views.AllPosts.as_view(), name="posts"),
    path("posts/<slug:slug>", views.SinglePost.as_view(), name="post_details"),
    path("read-later/",views.ReadLaterView.as_view(), name="read_later")
]
