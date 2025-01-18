from django.urls import path
from .. import views


urlpatterns = [
    path("comment/list/",views.CommentListView.as_view(),name="comment-list"),
    path("comment/<int:pk>/delete/",views.CommentDeleteView.as_view(),name="comment-delete"),
]