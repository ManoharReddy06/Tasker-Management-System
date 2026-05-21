import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'team_task_manager.settings')
django.setup()

from accounts.models import CustomUser
from projects.models import Project, ProjectMember
from tasks.models import Task

def seed_data():
    # Create Admin
    admin, created = CustomUser.objects.get_or_create(
        username='admin',
        defaults={'email': 'admin@example.com', 'role': 'admin'}
    )
    if created:
        admin.set_password('admin123')
        admin.save()
        print("Admin user created: admin / admin123")

    # Create Member
    member, created = CustomUser.objects.get_or_create(
        username='member1',
        defaults={'email': 'member1@example.com', 'role': 'member'}
    )
    if created:
        member.set_password('member123')
        member.save()
        print("Member user created: member1 / member123")

    # Create Project
    project, _ = Project.objects.get_or_create(
        name='Taskly Launch',
        defaults={
            'description': 'Launching our new task management app to the public.',
            'created_by': admin,
            'deadline': date.today() + timedelta(days=30),
            'status': 'active'
        }
    )

    # Add members to project
    ProjectMember.objects.get_or_create(project=project, user=admin, role='admin')
    ProjectMember.objects.get_or_create(project=project, user=member, role='member')

    # Create Tasks
    Task.objects.get_or_create(
        title='Design Database Schema',
        defaults={
            'description': 'Create the ERD and models for the core entities.',
            'project': project,
            'assigned_to': admin,
            'priority': 'high',
            'status': 'completed',
            'deadline': date.today() - timedelta(days=2)
        }
    )

    Task.objects.get_or_create(
        title='Build API Endpoints',
        defaults={
            'description': 'Implement REST APIs for projects and tasks.',
            'project': project,
            'assigned_to': member,
            'priority': 'medium',
            'status': 'in_progress',
            'deadline': date.today() + timedelta(days=5)
        }
    )

    Task.objects.get_or_create(
        title='Fix UI Bugs',
        defaults={
            'description': 'Resolve issues with responsive layout on mobile.',
            'project': project,
            'assigned_to': member,
            'priority': 'low',
            'status': 'pending',
            'deadline': date.today() + timedelta(days=10)
        }
    )

    print("Sample data seeded successfully!")

if __name__ == '__main__':
    seed_data()
