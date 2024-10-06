from typing import Any
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from utils.constants import Templates, Urls, ContextNames, Success
from utils.utils import get_api_stats, get_repository_star
from example.forms import BlogPostCreateForm
from django.urls import reverse_lazy
from example.models import BlogPost
from django.shortcuts import render
from django.contrib.messages import info


class IndexView(ListView):
    template_name = Templates.INDEX.value
    model = BlogPost
    context_object_name = ContextNames.BLOGS.value
    paginate_by = 10


index_view = IndexView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["hit"] = get_api_stats()
        context["stars"], context["updated"] = get_repository_star()
        return context


about_view = AboutView.as_view()


class BlogPostCreateView(CreateView):
    template_name = Templates.CREATE.value
    form_class = BlogPostCreateForm
    success_url = reverse_lazy(Urls.INDEX.value)

    def get_success_url(self) -> str:
        info(self.request, Success.CREATED.value)
        return super().get_success_url()


blog_post_create_view = BlogPostCreateView.as_view()


class BlogPostView(DetailView):
    template_name = Templates.BLOG.value
    model = BlogPost
    context_object_name = ContextNames.BLOG.value


blog_post_view = BlogPostView.as_view()


def custom_404(request, exception):
    return render(request, Templates.ERROR_404.value, status=404)


def custom_500(request):
    return render(request, Templates.ERROR_500.value, status=500)


def custom_403(request, exception):
    return render(request, Templates.ERROR_403.value, status=403)


def custom_400(request, exception):
    return render(request, Templates.ERROR_400.value, status=400)
