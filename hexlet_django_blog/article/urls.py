from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.apps import ArticleConfig

urlpatterns = [
    path('', views.ArticleView.as_view(), {"name": ArticleConfig.name}),
    path('<str:tags>/<int:article_id>/', views.ArticleView.as_view(), name="article"),
]
