from .models import Position
from django.forms import ModelForm, TextInput,Textarea


class PosForm(ModelForm):
    class Meta:
        model = Position
        fields = ["name", "type", "gramm", "sostav", "price"]
        widgets = {
            "name": TextInput(attrs={'placeholder': 'Название','class': 'form-input'}),
            "type": TextInput(attrs={'placeholder': 'Тип','class': 'form-input'}),
            "gramm": TextInput(attrs={'placeholder': 'Литры','class': 'form-input'}),
            "sostav": Textarea(attrs={'placeholder': 'Описание','class': 'form-input'}),
            "price": TextInput(attrs={'placeholder': 'Цена в руб.','class': 'form-input'}),
        }
