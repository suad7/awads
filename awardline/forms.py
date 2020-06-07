from django import forms
from .models import Project,Review,Comments
from django.core import validators


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['poster']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating','comment' ]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)