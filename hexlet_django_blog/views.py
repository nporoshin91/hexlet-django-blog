from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return redirect(reverse("article", kwargs={"tags": "python", "article_id": 42}))


def about(request):
    return render(request, "about.html")
