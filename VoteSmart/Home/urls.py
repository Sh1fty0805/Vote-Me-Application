from django.urls import path
from . import views

urlpatterns = [
    path('', views.CandidateListView.as_view(), name='candidate-list'),
    path('candidate/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate-detail'),
    path('candidate/create/', views.CandidateCreateView.as_view(), name='candidate-create'),
    path('candidate/<int:pk>/update/', views.CandidateUpdateView.as_view(), name='candidate-update'),
    path('candidate/<int:pk>/delete/', views.CandidateDeleteView.as_view(), name='candidate-delete'),
]