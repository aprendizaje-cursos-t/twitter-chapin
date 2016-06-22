from django import forms
from tweet import models


class TweetForm(forms.ModelForm):

    class Meta:
        model = models.Tweet
        fields = ('user', 'email', 'text',)

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
