from urllib import request
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UsersProfileSerializer, UserRegisterSerializer, VerifySerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersProfileSerializer
    queryset = Users.objects.all()


class Verify_EmailAPIView(generics.UpdateAPIView):
    serializer_class = VerifySerializer
    queryset = Users.objects.all()

    def post(self, request):
        user_obj = Users.objects.get(email=request.data.get('email'))
        serializer = VerifySerializer(user_obj, data=request.data)
        if serializer.is_valid():
            if Users.objects.filter(
                    verify_code=serializer.validated_data['token'],
                    email=serializer.validated_data['email']).exists():
                user_obj.is_active = True
                user_obj.verify_code_status = True
                serializer.save()
                return Response({'status': 'token is right, you`re verified'})
        return Response({'user': 'is created'})
