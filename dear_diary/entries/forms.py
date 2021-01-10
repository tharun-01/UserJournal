from django import forms
from .models import entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = entry
        fields = ['text', ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'textarea','placeholder':'whats on ur mind'})

