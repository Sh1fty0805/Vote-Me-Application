from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Candidate

class CandidateListView(ListView):
    model = Candidate
    template_name = 'candidate_list.html'

class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'candidate_detail.html'

class CandidateCreateView(CreateView):
    model = Candidate
    fields = '__all__'
    template_name = 'candidate_form.html'
    success_url = reverse_lazy('candidate-list')

class CandidateUpdateView(UpdateView):
    model = Candidate
    fields = '__all__'
    template_name = 'candidate_form.html'
    success_url = reverse_lazy('candidate-list')

class CandidateDeleteView(DeleteView):
    model = Candidate
    template_name = 'candidate_confirm_delete.html'
    success_url = reverse_lazy('candidate-list')

