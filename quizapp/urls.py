from django.urls import path
from . import views

urlpatterns = [
    path('',views.registration,name='registration'),
    path('login/',views.loginview,name='loginview'),
    path('login/',views.logoutview,name='logoutview'),
    # path('profile/',views.profile,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('quiz/create',views.create_quiz,name='create_quiz'),
    path('question_create/<int:id>',views.question_create,name='question_create'),
    path('show_questions/<int:id>',views.show_questions,name='show_questions'),

    path('quiz_edit/<int:id>',views.quiz_edit,name='quiz_edit'),


    
]
