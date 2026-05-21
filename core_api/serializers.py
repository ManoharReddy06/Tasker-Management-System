from rest_framework import serializers
from accounts.models import CustomUser
from projects.models import Project, ProjectMember
from tasks.models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'profile_picture', 'bio']

class ProjectSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.ReadOnlyField(source='assigned_to.username')
    project_name = serializers.ReadOnlyField(source='project.name')
    is_overdue = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = '__all__'
