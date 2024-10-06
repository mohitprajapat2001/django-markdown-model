from django.utils.translation import gettext_noop as _
from enum import Enum


# Settings Constants
# =====================================================
class Settings(Enum):
    ROOT_URL = "example.urls"
    TEMPLATE = "templates/"
    STATIC_URL = "static/"
    STATICFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    WSGI_APPLICATION = "example.wsgi.application"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    SECRET_KEY = "django-insecure-10830p2^=&%d_#gtvvc4y7jn*snprj*f8q&ela8t7ssug8k8vf"


# Success Messages
# =====================================================
class Success(Enum):
    CREATED = _("Post Created Successfully")

# Context Object Name
# =====================================================
class ContextNames(Enum):
    BLOGS = "blogs"
    BLOG = "blog"


# Templates Name
# =====================================================
class Templates(Enum):
    INDEX = "example/index.html"
    ABOUT = "example/about.html"
    CREATE = "example/create.html"
    BLOG = "example/blog.html"
    ERROR_404 = "errors/404.html"
    ERROR_403 = "errors/403.html"
    ERROR_400 = "errors/400.html"
    ERROR_500 = "errors/500.html"


# Urls Path & Reverse
# =====================================================
class Urls(Enum):
    INDEX = "index"
    ABOUT = "about"
    CREATE = "create"
    BLOG = "blog"


# Other Constants
# =====================================================
EMPTY_STR = ""
UTF_8 = "utf-8"
FORM_CLASS = "input input-bordered w-full"
FORM_CLASS_FILE = "file-input file-input-bordered w-full"
TEXT_AREA = "textarea textarea-bordered textarea-lg w-full"
SELECT_CLASS = "select select-bordered w-full select-sm"
THEME_CHOICES = (
    ("light", "light"),
    ("dark", "dark"),
    ("cupcake", "cupcake"),
    ("bumblebee", "bumblebee"),
    ("emerald", "emerald"),
    ("corporate", "corporate"),
    ("synthwave", "synthwave"),
    ("retro", "retro"),
    ("cyberpunk", "cyberpunk"),
    ("valentine", "valentine"),
    ("halloween", "halloween"),
    ("garden", "garden"),
    ("forest", "forest"),
    ("aqua", "aqua"),
    ("lofi", "lofi"),
    ("pastel", "pastel"),
    ("fantasy", "fantasy"),
    ("wireframe", "wireframe"),
    ("black", "black"),
    ("luxury", "luxury"),
    ("dracula", "dracula"),
    ("cmyk", "cmyk"),
    ("autumn", "autumn"),
    ("business", "business"),
    ("acid", "acid"),
    ("lemonade", "lemonade"),
    ("night", "night"),
    ("coffee", "coffee"),
    ("winter", "winter"),
    ("dim", "dim"),
    ("nord", "nord"),
    ("sunset", "sunset"),
)

TYPE_HTML = "text/html"
