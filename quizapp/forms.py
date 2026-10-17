from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    user_type = forms.ChoiceField(choices = CustomUser.user_type_choices, widget=forms.Select(attrs={'class':'form-control'}))
    field_order = ['username','email','password','confirm_password','user_type']
    class Meta:
         model = CustomUser
         fields = ['username','email','password','user_type']
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        fields = ['username','password']
        
class QuizForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Quiz
        fields = ['title','description']
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
    
    