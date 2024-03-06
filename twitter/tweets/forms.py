from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "What Is Happening?!",
                "class": "form-control",
                "rows": "2",
                "style": "width: 100%; background-color: black; color: grey; border: none;",
            }
        ),
        label="",
    )

    class Meta:
        model = Tweet
        exclude = ("user",)