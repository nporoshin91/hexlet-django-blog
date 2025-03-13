from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from hexlet_django_blog.articles.forms import ArticleForm
from hexlet_django_blog.articles.models import Article


class IndexView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, self.template_name, {"articles": articles})


class ArticleView(TemplateView):
    template_name = "articles/details.html"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs.get("article_id"))
        return render(request, self.template_name, {"article": article})


class ArticleFormCreateView(TemplateView):
    template_name = "articles/create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": ArticleForm()})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно создана!")
            return redirect("articles")

        messages.error(request, "Ошибка! Проверьте форму.")
        return render(request, self.template_name, {"form": form})


class ArticleFormEditView(TemplateView):
    template_name = "articles/edit.html"

    @staticmethod
    def get_article_by_id(**kwargs):
        return get_object_or_404(Article, id=kwargs.get("id"))

    def get(self, request, *args, **kwargs):
        form = ArticleForm(instance=self.get_article_by_id(**kwargs))
        return render(
            request,
            "articles/update.html",
            {"form": form, "article_id": kwargs.get("id")},
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST, instance=self.get_article_by_id(**kwargs))
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно обновлена!")
            return redirect("articles")

        messages.error(request, "Ошибка! Проверьте форму.")
        return render(
            request,
            "articles/update.html",
            {"form": form, "article_id": kwargs.get("id")},
        )
