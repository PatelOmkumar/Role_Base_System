from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authentication_module.serializers import UserRegrstrationSerializer, UserLoginSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer,UserDataViewSerializer,UserUpdateDetailsSerializer, AllUserDataViewSerializer
from common.middlewere import ExampleMiddleware
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from authentication_module.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from common.enums import Endpoint


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }



class UserRegistrationView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'date_of_birth': openapi.Schema(type=openapi.TYPE_STRING),
                'gender': openapi.Schema(type=openapi.TYPE_STRING),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'password2': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['email', 'name', 'phone', 'date_of_birth',
                      'gender', 'address', 'password', 'password2'],
        ),
        responses={
            200: openapi.Response('Response description', UserRegrstrationSerializer),
            400: "Bad request",
        }
    )
    def post(self, request):
        serializer = UserRegrstrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'your registration is successfully complited'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_verified = True
            user.save()
            return Response({'message': 'Email verification successfully complited.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid or expired verification link.'}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["email", "password"],
        ),
        responses={
            200: openapi.Response('Response description', UserLoginSerializer),
            400: "Bad request",
        }
    )
    def post(self, request, formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None and user.is_verified:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['email not validate or email or pwd are not validate']}}, status=status.HTTP_400_BAD_REQUEST)



class UserChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'old_password': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'password2': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['old_password', 'password', 'password2'],
        ),
        responses={
            200: openapi.Response('Response description', UserChangePasswordSerializer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',  # Name of the parameter
                openapi.IN_HEADER,  # Location of the parameter in the request
                description='Bearer token',  # Description of the parameter
                type=openapi.TYPE_STRING,  # Type of the parameter
                required=True,  # Whether the parameter is required
            )
        ]
    )
    def post(self, request, format=None):

        view_name = Endpoint.CHANGE_PASSWORD.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:
            serializer = UserChangePasswordSerializer(
                data=request.data, context={'user': request.user})
            if serializer.is_valid(raise_exception=True):
                return Response({'msg': 'password changed successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response


class SendPasswordResetEmailView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.FORMAT_EMAIL)
            },
            required=['email'],
        ),
        responses={
            200: openapi.Response('Response description', SendPasswordResetEmailSerializer),
            400: "Bad request",
        }
    )
    def post(self, request, format=None):

        view_name = Endpoint.SEND_RESET_PASSWORD_EMAIL.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:
            serializer = SendPasswordResetEmailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                return Response({'msg': ' Email send successfully check your mail to verify'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response


class UserPasswordRestView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'password2': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['password', 'password2'],
        ),
        responses={
            200: openapi.Response('Response description', UserPasswordResetSerializer),
            400: "Bad request",
        },
    )
    def post(self, request, uid, token, format=None):

        view_name = Endpoint.RESET_PASSWORD.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:
            serializer = UserPasswordResetSerializer(
                data=request.data, context={'uid': uid, 'token': token})
            if serializer.is_valid(raise_exception=True):
                return Response({'msg': 'password reseted successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response


class UserDataView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', UserDataViewSerializer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',  # Name of the parameter
                openapi.IN_HEADER,  # Location of the parameter in the request
                description='Bearer token',  # Description of the parameter
                type=openapi.TYPE_STRING,  # Type of the parameter
                required=True,  # Whether the parameter is required
            )
        ]
    )
    def get(self, request, *args, **kwargs):

        view_name = Endpoint.DATA_VIEW.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:
            serializer = UserDataViewSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response
            # Middleware returned an error response


class AllUserDataView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', AllUserDataViewSerializer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',  # Name of the parameter
                openapi.IN_HEADER,  # Location of the parameter in the request
                description='Bearer token',  # Description of the parameter
                type=openapi.TYPE_STRING,  # Type of the parameter
                required=True,  # Whether the parameter is required
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        view_name = Endpoint.ALL_USER_DATA_VIEW.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:

            users = User.objects.all()
            serializer = AllUserDataViewSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response
            # Middleware returned an error response


class UserUpdateDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.FORMAT_EMAIL),
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'date_of_birth': openapi.Schema(type=openapi.FORMAT_DATE),
                'gender': openapi.Schema(type=openapi.TYPE_STRING),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.FORMAT_PASSWORD),
                'password2': openapi.Schema(type=openapi.FORMAT_PASSWORD),
            },
            required=['email', 'name', 'phone', 'date_of_birth',
                      'gender', 'address', 'password', 'password2'],
        ),
        responses={
            200: openapi.Response('Response description', UserUpdateDetailsSerializer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',  # Name of the parameter
                openapi.IN_HEADER,  # Location of the parameter in the request
                description='Bearer token',  # Description of the parameter
                type=openapi.TYPE_STRING,  # Type of the parameter
                required=True,  # Whether the parameter is required
            )
        ]
    )
    def put(self, request, format=None):

        view_name = Endpoint.USER_UPDATE_DETAILS.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:
            seriazer = UserUpdateDetailsSerializer(
                data=request.data, context={'user': request.user})
            if seriazer.is_valid(raise_exception=True):
                return Response({'msg': 'User data updated successfully'}, status=status.HTTP_200_OK)
            return Response(seriazer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response


class UserDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description'),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',  # Name of the parameter
                openapi.IN_HEADER,  # Location of the parameter in the request
                description='Bearer token',  # Description of the parameter
                type=openapi.TYPE_STRING,  # Type of the parameter
                required=True,  # Whether the parameter is required
            )
        ]
    )
    def delete(self, request, format=None):

        view_name = Endpoint.USER_DELETE.value

        django_request = HttpRequest()
        django_request.method = request.method
        django_request.GET = request.query_params
        django_request.POST = request.data
        django_request.user = request.user
        # Set this attribute to True to disable CSRF checks
        django_request._dont_enforce_csrf_checks = True

        middleware = ExampleMiddleware(get_response=self.dispatch)
        response = middleware(django_request, view_name=view_name)

        if response.status_code == 200:

            user = request.user  # Get authenticated user
            user.delete()
            return Response({'msg': 'User deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return response
