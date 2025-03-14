from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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

    @staticmethod
    def get_article_by_id(**kwargs):
        return get_object_or_404(Article, id=kwargs.get("article_id"))

    def get(self, request, *args, **kwargs):
        article = self.get_article_by_id(**kwargs)
        return render(request, self.template_name, {"article": article})

    def delete(self, request, *args, **kwargs):
        article = self.get_article_by_id(**kwargs)
        if article:
            article.delete()
            messages.success(request, "Статья успешно удалена!")
            return JsonResponse({"redirect_url": reverse("articles")}, status=200)

        messages.error(request, "Произошла ошибка при удаление статьи.")
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
    template_name = "articles/update.html"

    @staticmethod
    def get_article_by_id(**kwargs):
        return get_object_or_404(Article, id=kwargs.get("article_id"))

    def get(self, request, *args, **kwargs):
        form = ArticleForm(instance=self.get_article_by_id(**kwargs))
        return render(
            request,
            self.template_name,
            {"form": form, "article_id": kwargs.get("article_id")},
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
            self.template_name,
            {"form": form, "article_id": kwargs.get("article_id")},
        )
