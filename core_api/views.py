from rest_framework import viewsets, permissions
from projects.models import Project
from tasks.models import Task
from accounts.models import CustomUser
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            return Project.objects.all()
        return Project.objects.filter(members__user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            return Task.objects.all()
        return Task.objects.filter(assigned_to=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
