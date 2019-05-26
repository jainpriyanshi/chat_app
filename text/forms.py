from django import forms

from .models import Text

class PostForm(forms.ModelForm):

    class Meta:
        model = Text
        fields = ('message','img',)