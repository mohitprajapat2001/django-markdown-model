from django.template import Library
from datetime import datetime, timedelta, timezone

register = Library()


@register.simple_tag
def format_number(value, *args, **kwargs):
    try:
        value = int(value)
        for unit in ["", "K", "M", "B", "T"]:
            if abs(value) < 1000.0:
                return f"{value:6.2f}{unit}"
            value /= 1000.0
        return f"{value:6.2f}B"
    except TypeError:
        return "Nan"


@register.simple_tag
def time_ago(timestamp):
    now = datetime.now(timezone.utc)
    timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

    delta = now - timestamp

    if delta < timedelta(minutes=1):
        return "recently"
    elif delta < timedelta(hours=1):
        return f"{int(delta.total_seconds() // 60)} minutes ago"
    elif delta < timedelta(days=1):
        hours = delta.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif delta < timedelta(days=2):
        return "yesterday"
    elif delta < timedelta(days=30):
        days = delta.days
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return "long time ago"
