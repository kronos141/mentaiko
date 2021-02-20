from django.shortcuts import render, redirect
from django import forms
from .models import StudentUser,MyUserManager


def signup(request):
    if request.method == 'POST':
        print(request.method)
        email = request.POST['email']
        password = request.POST['enter_password']
        username_family = request.POST['username_family']
        username_first = request.POST['username_first']
        grade = request.POST['grade']
        department = request.POST['department']
        print(email,password,username_family,department)
        newuser = StudentUser.objects.create_user(
            username_family=username_family,
            username_first=username_first,
            grade=grade,
            department=department,
            email=email,
            password=password)
        return redirect('home')
    
    else:
        print('fail')
        return render(request, 'signup.html')


class SignUpForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput)
    enter_password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if StudentUser.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_password', 'This does not match with the above.')

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('enter_password')
        username_family = self.cleaned_data.get('username_family')
        username_first = self.cleaned_data.get('username_first')
        grade = self.cleaned_data.get('grade')
        department = self.cleaned_data.get('department')

        newuser = MyUserManager.create_user(
            username_family=username_family,
            username_first=username_first,
            grade=grade,
            department=department,
            email=email,
            password=password)

