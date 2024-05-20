from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "What s Happening?!",
                "class": "form-control",
                "rows": "2",
                "style": "width: 100%; margin-bottom: 0; margin-left: 15%; background-color: black; color: grey; border-bottom: 1px solid grey; border-top: none;  border-right: none; border-left: none;",
            }
        ),
        label="",
    )

    class Meta:
        model = Tweet
        exclude = ("user",)
