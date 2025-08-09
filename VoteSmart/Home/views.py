from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Candidate
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('candidate-list')  # Redirect after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('candidate-list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


class CandidateListView(ListView):
    model = Candidate
    template_name = 'candidate_list.html'

class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'candidate_detail.html'

class CandidateCreateView(LoginRequiredMixin, CreateView):
    model = Candidate
    fields = '__all__'
    template_name = 'candidate_form.html'
    success_url = reverse_lazy('candidate-list')
    login_url = 'login'

class CandidateUpdateView(LoginRequiredMixin, UpdateView):
    model = Candidate
    fields = '__all__'
    template_name = 'candidate_form.html'
    success_url = reverse_lazy('candidate-list')
    login_url = 'login'

class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    model = Candidate
    template_name = 'candidate_confirm_delete.html'
    success_url = reverse_lazy('candidate-list')
    login_url = 'login'

