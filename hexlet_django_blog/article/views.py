from hexlet_django_blog.views import IndexView


class ArticleView(IndexView):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        return super(ArticleView, self).get_context_data(**kwargs)
