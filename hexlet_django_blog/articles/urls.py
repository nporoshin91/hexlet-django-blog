from django.urls import path

from hexlet_django_blog.articles import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="articles"),
    path("<int:id>/edit/", views.ArticleFormEditView.as_view(), name="article_update"),
    path("<int:article_id>/", views.ArticleView.as_view(), name="article"),
    path("create/", views.ArticleFormCreateView.as_view(), name="article_create"),
]
