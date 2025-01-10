from django.urls import path, include
from .views import*

app_name = "review"

urlpatterns = [
        path("submit-review/",SubmitReviewView.as_view(),name="submit-review")
]
