from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


def about(request):
    return render(request, "about.html")
