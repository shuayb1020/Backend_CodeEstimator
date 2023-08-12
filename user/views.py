from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from rest_framework import routers, serializers, viewsets, generics, permissions
from .serializers import *
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
# from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password


class Register(APIView):
    # permission_classes = (permissions.AllowAny,)
    parser_classes = [JSONParser]
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            obj = serializer.save()
            password = make_password(serializer.data['password'])
            User.objects.filter(email = serializer.data['email']).update(password = password)
            return Response({'success': 'Regsitration Successful'})
        else:
            return Response({'error': "Error, try again"})

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        check_email = User.objects.filter(username = username).exists()
        if check_email == False:
            return Response({'error': 'No account with this username'})
        user = User.objects.get(username = username)
        if user.check_password(password) == False:
            return Response({'error': 'Password not correct'})
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, log_user)
            return Response({'success' : 'LoginSuccessful'})
        else:
            return Response({'error': 'Invalid email/password'},  status=400)

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
	
	def post(self, request):
		serializer = UserRegisterSerializer(data = request.data)
		if serializer.is_valid():
			obj = serializer.save()
			password = make_password(serializer.data['password'])
			User.objects.filter(email = serializer.data['email']).update(password = password)
			return Response({'success': 'Regsitration Successful'})
		else:
			return Response({'error': "Error, try again"})
