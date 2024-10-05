# Django Markdown Model Constants
from enum import Enum
from django.utils.translation import gettext_noop as _


class MarkdownModelConstants(Enum):
    """Markdown Model Constants"""

    FIELD_DESCRIPTION = _("Markdown Text")
