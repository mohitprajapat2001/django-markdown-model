from django.contrib.admin import site
from example.models import BlogPost, Stats

site.register(Stats)
site.register(BlogPost)
