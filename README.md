# Django Markdown Model

Django Markdown Model is a Python project that provides a simple way to integrate a Markdown field into your Django models. This package allows you to store and render Markdown content effortlessly, making it ideal for applications that require rich text input from users.

## Features

- **MarkdownField**: Easily store and manage Markdown content in your Django models.
- **Simple Integration**: Quick setup and integration into existing Django projects.
- **Flexible Rendering**: Supports various Markdown renderers for displaying content.

## Installation

You can install this package via pip:

```bash
pip install django-markdown-model
```

## Usage

To use this package in your Django project, follow these steps:

1. **Add django_markdown_model to your INSTALLED_APPS** in your Django settings:

```python
INSTALLED_APPS = [
...
'django_markdown_model',
]
```

2. **Create your models using MarkdownField**:

```python
from django.db import models
from django_markdown_model.fields import MarkdownField

class MyModel(models.Model):
title = models.CharField(max_length=200)
content = MarkdownField()

       def __str__(self):
           return self.title
```

3. **Use Abstract Model MarkdownModel**:

```python
from django.db import models
from django_markdown_model.fields import MarkdownField

class MyModel(MarkdownModel):
pass
```

4. **Render Markdown in your templates**:

   Use a Markdown renderer (like markdown2 or mistune) to display the content:

```html
<h1>{{ my_model.title }}</h1>
<div>{{ my_model.content|safe }}</div>
```

## Example

See the examples/ directory for a complete example of how to use this package in a Django project.

## Running Tests

Tests are under development.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
