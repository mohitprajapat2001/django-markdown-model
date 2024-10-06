from example.forms import Themes, NewsLetter


def theme_form(request):
    theme_form = Themes()
    return {"theme_form": theme_form}


def newsletter_form(request):
    newsletter_form = NewsLetter()
    return {"newsletter_form": newsletter_form}
