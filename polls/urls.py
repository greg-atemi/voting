from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:election_id>/", views.detail, name="detail"),
    path("<int:election_id>/results/", views.results, name="results"),
    path("<int:election_id>/vote/", views.vote, name="vote"),
]