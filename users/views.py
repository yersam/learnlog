from django.shortcuts import render,reverse

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method=='POST':
        """显示空的注册表单"""
        form = UserCreationForm()
    else:
        """处理填写好的表单"""
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('index'))

        return render(request,'register.html',locals())