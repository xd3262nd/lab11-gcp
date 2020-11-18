from django import forms
from .models import Places


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ('name', 'visited')


class DateInput(forms.DateInput):
    input_type = 'date'


class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ('notes', 'date_visited','photo')
        widgets = {
            'date_visited': DateInput()
        }