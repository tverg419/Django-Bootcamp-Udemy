from django.shortcuts import render
from second_app.models import UserInfo
from second_app.forms import UserForm

def index(request):
    return render(request, 'second_app/index.html')

def users(request):
    users_list = UserInfo.objects.order_by('first_name')
    user_dict ={"user_content":users_list}
    return render(request, 'second_app/users.html', context=user_dict)

def signup(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")

    return render(request, 'second_app/signup.html',{'form':form})
