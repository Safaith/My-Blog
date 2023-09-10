from django import forms
from .models import comment

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        exclude = ["post"]
        labels = {
          "user_name":"your name",
          "user_email":"your email",
          "text":"your comment"
        }