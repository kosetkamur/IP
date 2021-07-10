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
        fields = '__all__'

        

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')

        return new_slug
