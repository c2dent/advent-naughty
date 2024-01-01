from django import forms

from main.models import PlannedMessage, Cell


class PlannedMessageForm(forms.ModelForm):
    class Meta:
        model = PlannedMessage
        fields = '__all__'


class CellMessageForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = '__all__'
