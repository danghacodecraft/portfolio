from django.forms import ModelForm
from django import forms
from .models import Comment, Endorsement, Project, Message, Skill


class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'body']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })


class MessageForm(ModelForm):
    name = forms.CharField(max_length=200, label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.CharField(max_length=200, label='Email', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    subject = forms.CharField(max_length=200, label='Subject', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    body = forms.CharField(max_length=200, label='Body', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
        'style': 'resize:none',
    }))

    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })


class EndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
        fields = '__all__'
        exclude = ['featured']
    
    def __init__(self, *args, **kwargs):
        super(EndorsementForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['project']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', }
        )
