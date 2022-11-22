from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Users
from .serializers import (
    UsersProfileSerializer,
    UserRegisterSerializer,
    VerifySerializer,
    ChangePasswordSerializer,
)


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


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = Users
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
