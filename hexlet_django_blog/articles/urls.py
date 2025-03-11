from django.urls import path

from hexlet_django_blog.articles import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("<int:article_id>/", views.ArticleView.as_view(), name="article"),
]
