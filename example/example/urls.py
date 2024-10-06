from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler403, handler404, handler500
from utils.constants import Urls
from example.views import index_view, about_view, blog_post_create_view, blog_post_view
from example.settings import STATIC_ROOT, STATIC_URL, DEBUG
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name=Urls.INDEX.value),
    path("about/", about_view, name=Urls.ABOUT.value),
    path("create/", blog_post_create_view, name=Urls.CREATE.value),
    path("blog/<int:pk>", blog_post_view, name=Urls.BLOG.value),
]


# Custom error handlers
handler404 = "example.views.custom_404"
handler500 = "example.views.custom_500"
handler403 = "example.views.custom_403"
handler400 = "example.views.custom_400"
urlpatterns = urlpatterns + static(STATIC_URL, document_root=STATIC_ROOT)
