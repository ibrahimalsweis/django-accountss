from django.forms import ModelForm
from .models import Post

class FormUploadImage(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        