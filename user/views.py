from django.shortcuts import render, redirect
from .forms import CustomCsUserChangeForm
from django.contrib import messages

def profile_view(request):
    if request.method == 'GET':
        return render(request, 'profile.html')

def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomCsUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'profile.html')
    else:
        user_change_form = CustomCsUserChangeForm(instance = request.user)
        return render(request, 'profile_update.html', {'user_change_form':user_change_form})

def profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/user/profile')
    return render(request, 'profile_delete.html')
