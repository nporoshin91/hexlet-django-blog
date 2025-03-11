from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from hexlet_django_blog.articles.models import Article


class IndexView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, self.template_name, {"articles": articles})


class ArticleView(TemplateView):
    template_name = "articles/article_details.html"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs.get("article_id"))
        return render(request, self.template_name, {"article": article})
