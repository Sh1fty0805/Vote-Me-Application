from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Candidate
from .models import UserProfile
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('candidate-list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required

def landing_view(request):
    # You can later merge signup + login modals here
    return render(request, "landing.html")

@login_required
def home_view(request):
    return render(request, "home.html")

@login_required
def candidates_view(request):
    # This could be just a template with static candidate categories for now
    return render(request, "candidates.html")

@login_required
def profile_view(request):
    profile = None
    if hasattr(request.user, 'userprofile'):
        profile = request.user.userprofile
    return render(request, "profile.html", {"profile": profile})






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

