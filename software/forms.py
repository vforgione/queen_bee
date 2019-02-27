from django import forms

from .models import Software


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
        widgets = dict(
            name=forms.TextInput(),
            version=forms.TextInput(),
            source_url=forms.URLInput(),
            docs_url=forms.URLInput(),
        )
