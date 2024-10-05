from typing import Any
from django.db.models import Model
from django.utils.translation import gettext_lazy as _
from markdown import markdown
from django_markdown_model.utils.constants import MarkdownModelConstants
from django_markdown_model.fields import MarkDownField


class MarkdownModel(Model):
    """Base Markdown Model Class"""

    content = MarkDownField(blank=True, null=True)

    class Meta:
        abstract = True
