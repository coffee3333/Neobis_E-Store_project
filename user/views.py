# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import UserSerializer, LoginSerializer
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from rest_framework_simplejwt.tokens import RefreshToken



# @swagger_auto_schema(
#     method='post',
#     request_body=UserSerializer,  # Указываем, что тело запроса должно быть сериализовано с помощью LoginSerializer
#     responses={
#         200: openapi.Response('Successful Login', UserSerializer),
#         400: 'Invalid Credentials'
#     }
# )

# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @swagger_auto_schema(
#     method='post',
#     request_body=LoginSerializer,
#     responses={
#         200: openapi.Response('Successful Login', LoginSerializer),
#         400: 'Invalid Credentials'
#     }
# )

# @api_view(['POST'])
# def login(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     refresh = RefreshToken.for_user(user)

#     return Response({
#         'user': user.username,
#         'access_token': str(refresh.access_token),
#         'refresh_token': str(refresh),
#     })



from django.contrib.auth import login, logout

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': user.username,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }, status=status.HTTP_202_ACCEPTED)
    

class LogoutView(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user