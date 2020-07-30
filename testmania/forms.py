from django import forms

class FiveToSix(forms.Form):
    input_grade = forms.IntegerField(max_value=6)
    output_grade = forms.IntegerField(max_value=6, required=False)
    