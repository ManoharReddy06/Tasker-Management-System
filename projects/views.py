from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Project, ProjectMember
from tasks.models import Task

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        if self.request.user.is_admin():
            return Project.objects.all()
        return Project.objects.filter(members__user=self.request.user)

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        context['members'] = self.object.members.all()
        return context

class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'deadline', 'status']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')

    def test_func(self):
        return self.request.user.is_admin()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'deadline', 'status']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')

    def test_func(self):
        return self.request.user.is_admin()

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:list')

    def test_func(self):
        return self.request.user.is_admin()
