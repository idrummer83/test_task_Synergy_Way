from .models import SynergyUser, SynergyGroup
from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class UsersListView(generics.ListAPIView):
    queryset = SynergyUser.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = SynergyUser.objects.all()
    serializer_class = UserSerializer


class UsersEditView(generics.RetrieveUpdateAPIView):
    queryset = SynergyUser.objects.all()
    serializer_class = UserSerializer


class UsersDeleteView(generics.RetrieveDestroyAPIView):
    queryset = SynergyUser.objects.all()
    serializer_class = UserSerializer


class UserGroupListView(generics.ListAPIView):
    queryset = SynergyGroup.objects.all()
    serializer_class = GroupSerializer


class UserGroupCreateView(generics.CreateAPIView):
    queryset = SynergyGroup.objects.all()
    serializer_class = GroupSerializer


class UserGroupEditView(generics.RetrieveUpdateAPIView):
    queryset = SynergyGroup.objects.all()
    serializer_class = GroupSerializer


class UserGroupDeleteView(generics.RetrieveDestroyAPIView):
    queryset = SynergyGroup.objects.all()
    serializer_class = GroupSerializer

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        yusik = SynergyUser.objects.filter(synergy_group_id=kwargs['pk']).first()
        if yusik:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
