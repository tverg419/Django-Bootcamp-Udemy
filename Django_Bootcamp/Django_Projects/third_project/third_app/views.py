from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'third_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST': # Must be Capitalized!
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("\n")
            print("Validation Success")
            print("Name: "+form.cleaned_data['name'])
            print("E-mail: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])


    return render(request,'third_app/form.html',{'form':form})
