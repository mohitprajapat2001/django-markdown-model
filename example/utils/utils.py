def get_repository_star():
    """
    get github repository star count
    """
    from requests import get

    response = get(
        "https://api.github.com/repos/mohitprajapat2001/django-markdown-model"
    ).json()
    return response.get("stargazers_count"), response.get("updated_at")


def get_api_stats():
    """
    get api stats information
    """
    from example.models import Stats

    try:
        hit = Stats.objects.first().hit
    except AttributeError:
        Stats.objects.create()
        hit = Stats.objects.first().hit
    return hit
