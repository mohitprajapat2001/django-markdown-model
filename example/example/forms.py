from django import forms
from utils.constants import THEME_CHOICES, SELECT_CLASS, FORM_CLASS, TEXT_AREA
from example.models import BlogPost


class Themes(forms.Form):
    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        widget=forms.Select(
            attrs={
                "class": SELECT_CLASS,
                "id": "themeSelect",
                "required": False,
            }
        ),
    )


class NewsLetter(forms.Form):
    subscribe = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "grow", "type": "email"})
    )


class BlogPostCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": FORM_CLASS}),
            "content": forms.Textarea(attrs={"class": TEXT_AREA}),
        }
        labels = {"title": "Enter Post Title", "content": "Enter Post Content"}

    field_order = ["title", "content"]
