from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, EditProfileForm
  
    
class SignUpView(CreateView):
    form_class = NewUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    

class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    success_url = reverse_lazy('index')
    template_name = 'registration/profile.html'
    
    
    
    