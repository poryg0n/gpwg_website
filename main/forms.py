from django import forms
from .models import NewItem

class CreateNewNews(forms.ModelForm):

    class Meta:
        model = NewItem
#       fields = "__all__"
#       exclude = ['posts','author','slug']
        exclude = ['author']
