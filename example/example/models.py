from django.db.models import Model, IntegerField, CharField, DateTimeField
from django_markdown_model.models import MarkdownModel
from django.utils.timezone import now


class Stats(Model):
    """website users hit"""

    hit = IntegerField(default=0)


class BlogPost(MarkdownModel):
    title = CharField(max_length=264)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Blog {id}".format(id=self.id)
