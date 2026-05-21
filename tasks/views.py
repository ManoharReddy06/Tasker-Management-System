from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Task, TaskComment
from projects.models import Project

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.all()
        if not self.request.user.is_admin():
            queryset = queryset.filter(assigned_to=self.request.user)
        
        # Filtering
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
            
        return queryset

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context

class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'project', 'assigned_to', 'priority', 'status', 'deadline']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def test_func(self):
        return self.request.user.is_admin()

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'status', 'deadline']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def test_func(self):
        task = self.get_object()
        # Admin can edit anything, Member can only update status/basic info if assigned
        return self.request.user.is_admin() or task.assigned_to == self.request.user

    def get_form_class(self):
        from django import forms
        form_class = super().get_form_class()
        if not self.request.user.is_admin():
            # Members can only update status
            class MemberTaskForm(form_class):
                class Meta(form_class.Meta):
                    fields = ['status']
            return MemberTaskForm
        return form_class

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')

    def test_func(self):
        return self.request.user.is_admin()
