from django import forms
from django.forms import ModelForm

from .models import Profile, Comment, FeedBack


class CustomerForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','insta','facebook',)
        exclude = ['user']


class CommentForm(ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'комментарий...', 'rows': '4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'phone', 'description',)