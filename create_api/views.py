from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import UserForm, JokesForm 

def process_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']
            return HttpResponse(f'{name} is {age} years old and earns {salary} every month')
    else:
        form = UserForm()
    return render(request, 'templates/form.html', {'form': form})

def fetch_jokes(request):
    if request.method == 'POST':
        form = JokesForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['count']
            headers = {
                'X-Api-Key':'ZaDXxdAiapsdX+oDVEZODg==U4btY8xgNPxI2j9C'
            }
            response = requests.get(f'https://api.api-ninjas.com/v1/jokes?limit={count}', headers=headers)
            jokes = response.json()
            return render(request, 'create_api\templates\jokes.html', {'jokes': jokes})
    else:
        form = JokesForm()
    return render(request, 'create_api\templates\jokes.html', {'form': form})
