from django import forms
from .models import Data


class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = (
            'fio',
            'carnumber',
            'regdata',
            'tirnumber',
            'waybill',
            'cmr1',
            'cmr2',
            'dazvol',
            'tc',
            'tircheck',
            'waybillcheck',
            'cmr1check',
            'cmr2check',
            'dcheck',
            'tcheck',
            'checker',
        )
        widgets = {
            'fio': forms.TextInput,
            'tirnumber': forms.TextInput,
            'waybill': forms.TextInput,
            'cmr1': forms.TextInput,
            'cmr2': forms.TextInput,
            'dazvol': forms.TextInput,
            'tc': forms.TextInput,
        }