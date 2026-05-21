from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from django.utils import timezone
from django.db.models import Count

@login_required
def home_view(request):
    user = request.user
    if user.is_admin():
        projects = Project.objects.all()
        tasks = Task.objects.all()
    else:
        projects = Project.objects.filter(members__user=user)
        tasks = Task.objects.filter(assigned_to=user)

    total_projects = projects.count()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status='pending').count()
    overdue_tasks = [task for task in tasks if task.is_overdue]
    overdue_count = len(overdue_tasks)

    # Chart data
    status_counts = tasks.values('status').annotate(count=Count('status'))
    
    context = {
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_count': overdue_count,
        'recent_tasks': tasks.order_by('-created_at')[:5],
        'status_counts': status_counts,
    }
    return render(request, 'dashboard/home.html', context)
