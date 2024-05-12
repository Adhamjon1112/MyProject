from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Note

User = get_user_model()


class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'p-2 border border-slate-500 rounded w-full',
    }), label="Parol")
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'p-2 border border-slate-500 rounded w-full',
    }), label="Parolni tasdiqlang")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
            'username': forms.TextInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'border rounded-lg p-2 w-full'})
        self.fields['description'].widget.attrs.update({'class': 'border rounded-lg p-2 w-full'})
        if user:
            self.instance.owner = user


# class NoteForm(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = ['title', 'description']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update({'class': 'border rounded-lg p-2 w-full'})
#         self.fields['description'].widget.attrs.update({'class': 'border rounded-lg p-2 w-full'})
