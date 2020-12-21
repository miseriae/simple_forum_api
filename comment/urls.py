from django.urls import path

from . import views


urlpatterns = [
    path("", views.CommentView.as_view()),
    path("<int:pk>/", views.CreateCommentView.as_view()),
]
