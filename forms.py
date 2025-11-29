
from django import forms
class StudentInputForm(forms.Form):
    hours_studied = forms.FloatField()
    attendance = forms.FloatField()
    previous_score = forms.FloatField()
    assignments_completed = forms.IntegerField()
