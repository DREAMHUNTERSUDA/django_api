from django import forms

class userForm(forms.Form):
    name= forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=1)
    salary=forms.IntegerField(min_value=1)

class JokesForm(forms.Form):  
    count = forms.IntegerField(min_value=1, max_value=10)    