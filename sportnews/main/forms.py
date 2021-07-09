from .models import Review
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from django import forms


class ScoreFilter(forms.Form):
    score_min = forms.IntegerField(label="От", required=False)
    score_max = forms.IntegerField(label="До", required=False)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["name", "content", "score"]
        widgets = {
            "name": TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            
            "content": Textarea(attrs={
                'id': 'content',
                'class': 'form-control',
                'placeholder': 'Введите отзыв'
            }),
            "score": NumberInput(attrs={
                'id': 'score',
                'class': 'form-control',
                'placeholder': 'Введите оценку'
            })
        }