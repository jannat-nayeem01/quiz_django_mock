from django.shortcuts import render,redirect
from .models import *
from .forms import RegistrationForm,LoginForm,QuizForm,QuestionForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def registration(request):
    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if (password != confirm_password):
                messages.error(request,'Password does not match')
                return redirect('registration')
            user.set_password(password)
            user.save()
            messages.success(request,'Registration Done!')
            return redirect('loginview')
            
            
    form = RegistrationForm()
    return render(request,'registration.html',{'form':form})

def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password = password)
            if user is not None:
                login(request,user)
                messages.success(request,'Your are logged in!')
                return redirect('dashboard')
    form = LoginForm()
    return render(request,'login.html',{'form':form})
def logoutview(request):
    logout(request)
    messages.success(request,'You are logged Out!')
    return redirect('loginview')
    
def dashboard(request):
    if request.user.user_type == 'admin':
        return render(request,'dashboard.html')
    else:
        participant,created = Participant.objects.get_or_create(user = request.user)
        return render(request,'dashboard.html')
    
def create_quiz(request):
    quiz = Quiz.objects.all()
    if request.method == 'POST':
        form  = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Quiz Created Successfully!')
            return redirect('create_quiz')
            

    form  = QuizForm()
    return render(request,'create_quiz.html',{'form':form,'quizes':quiz})
    
def quiz_edit(request,id):
    quiz = Quiz.objects.get(id=id)
    if request.method == 'POST':
        form  = QuizForm(request.POST,instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request,'Quiz Updated Successfully!')
            return redirect('create_quiz')
            

    form  = QuizForm(instance=quiz)
    return render(request,'manage_quiz.html',{'form':form})

def question_create(request,id):
    if request.method=='POST':
        quiz = Quiz.objects.get(id=id)
        if quiz is not None:
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit= False)
                question.quiz = quiz
                form.save()
                messages.success(request,'Question Created Successfully!')

            
    form = QuestionForm()
    return render(request,'create_question.html',{'form':form})
def show_questions(request,id):
    quiz = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz = quiz)
    context = {
        'questions':questions
    }
    return render(request,'show_questions.html',{'context':context})
    
    