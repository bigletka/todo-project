
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action == 'list':
            return Task.objects.filter(user=self.request.user)
        return super().get_queryset()

    @action(detail=True, methods=['post'])
    def mark_as_completed(self, request, pk=None):
        task = self.get_object()
        task.status = 'COMPLETED'
        task.save()
        return Response({'status': 'task marked as completed'})

    def filter_queryset(self, queryset):
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
