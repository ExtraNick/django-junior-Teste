from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

#Comentario codigo pre-tutorial django 4
# from . import views

# app_name = "polls"
# urlpatterns = [
#     # ex:/polls/ <- default page
#     path("", views.index, name="index"),
#     # ex: /polls/5/ <- page of a poll's id
#     path("<int:question_id>/", views.detail, name="detail"),
#     #ex: /polls/5/results/ <- page of results of a poll's id
#     path("<int:question_id>/results/", views.results, name="results"),
#     #ex: /polls/5/vote/ <- display votes of a poll's id
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]