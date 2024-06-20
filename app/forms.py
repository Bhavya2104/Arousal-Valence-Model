from django import forms

class ArousalForm(forms.Form):
    CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    CHOICES1 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    CHOICES2 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    Arousal = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    Valence = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES1, 
    )
    Intensity = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES2, 
    )
