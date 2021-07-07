from django import forms
from .models import  Category, Post
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Post
        cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, to_field_name="category")
        fields = ['title', 'time_to_cook', 'count', 'image','slug', 'body', 'cat']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'time_to_cook': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')

        return new_slug
