from django import forms

from .models import Node, NodeHardware


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = '__all__'
        widgets = dict(
            id=forms.TextInput(),
            name=forms.TextInput(),
            address=forms.TextInput(),
            modem_imei=forms.TextInput(),
            sim_iccid=forms.TextInput(),
            ssh_port=forms.TextInput(),
        )


class NodeHardwareForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = '__all__'
        widgets = dict(
            name=forms.TextInput(),
        )
