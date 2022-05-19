from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import SignupForm, ProfileForm , UserForm
from django.contrib.auth import authenticate , login
def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password= form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    
    conttext= {
        'form':form
    }
    return render(request,'registration\signup.html',conttext)


@login_required
def profile(request):

    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration\profile.html',{'profile':profile})


def profile_edit(request):  
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST ,instance=profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            # myform = profile_form.save(commit=False)
            # myform.user = request.user
            profile_form.save()
            return redirect('/accounts/profile')

    else:
        profile_form = ProfileForm(instance=request.user)
        user_form = UserForm(instance=request.user)
    return render(request, 'registration\profile_edit.html',{'profile_form':profile_form,'user_form':user_form})

