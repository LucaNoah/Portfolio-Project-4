from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article


class ArticleList(generic.ListView):
  model = Article
  queryset = Article.objects.filter(status=1, approved=True).order_by('-created_date')
  template_name = 'index.html'
  paginate_by = 8


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1, approved=True)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by("-created_date")

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
            },
        )


def create_article(request):
    return render(request, 'create_article.html')