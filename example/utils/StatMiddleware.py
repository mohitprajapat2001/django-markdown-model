from example.models import Stats
from django.db.models import F


class StatMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        stats = Stats.objects.first()
        if stats:
            stats.hit = F("hit") + 1
            stats.save(update_fields=["hit"])
        response = self.get_response(request)

        return response
