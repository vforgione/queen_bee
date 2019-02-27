from django import forms

from .models import Component, Instance


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'
        widgets = dict(
            name=forms.TextInput(),
            manufacturer=forms.TextInput(),
            version=forms.TextInput(),
            part_number=forms.TextInput(),
            parameter=forms.TextInput(),
            raw_data_type=forms.TextInput(),
            vsr_data_type=forms.TextInput(),
            vsr_unit=forms.TextInput(),
        )


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = '__all__'
        widgets = dict(
            uid=forms.TextInput(),
        )
