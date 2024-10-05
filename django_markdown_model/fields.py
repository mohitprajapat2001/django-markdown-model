from typing import Any
from django.db.models import Model
from django.db.models import TextField
from django.utils.translation import gettext_lazy as _
from markdown import markdown
from django_markdown_model.utils.constants import MarkdownModelConstants


class MarkDownField(TextField):
    """Base Markdown Model Field"""

    description = MarkdownModelConstants.FIELD_DESCRIPTION.value

    def clean(self, value: Any, model_instance: Model | None) -> Any:
        if value:
            value = markdown(value)
        return super().clean(value, model_instance)
