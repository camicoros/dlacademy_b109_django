from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class SubscribeForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tag', 'image', 'title', 'description']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image.size >= 5 * 1024 * 1024:
            raise ValidationError("File is too big!", code='size_error')

        return image
