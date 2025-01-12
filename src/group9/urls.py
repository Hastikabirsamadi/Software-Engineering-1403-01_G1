from django.urls import path
from .views import *

app_name = 'group9'
urlpatterns = [
  path('', home, name='group9'),
  path('signup/',sign_up_user, name='Signup'),
  path('login/', login_user, name='login'),
  path('main/', mainpage, name='main'),
  path('start_exam/', start_exam, name='start_exam'),
  path('questions/', show_questions, name='show_questions')
] 