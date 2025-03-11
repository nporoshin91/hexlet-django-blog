from django.shortcuts import render
from django.views.generic import TemplateView

from hexlet_django_blog.articles.models import Article


class ArticleView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()[:15]
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
