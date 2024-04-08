from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import generics
from django.urls import reverse_lazy
from common.middlewere import ExampleMiddleware
from user_permission.serializers import UserPermissionSerilizer
from rest_framework import permissions
from django.utils.encoding import smart_str
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from user_permission.models import  UserPermission
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from common.enums import Endpoint


class GetAllUserPermission(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]

    # queryset = UserPermission.objects.all()
    # serializer_class = UserPermissionSerilizer

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', UserPermissionSerilizer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer token',
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):

        view_name = Endpoint.GET_ALL_USER_PERMISSION.value

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
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return response
        

class CreateUserPermission(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerilizer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['user_id', 'permission_id'],
        ),
        responses={
            201: openapi.Response('Response description', UserPermissionSerilizer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer token',
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        view_name = Endpoint.CREATE_USER_PERMISSION.value

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
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return response


class UpdateUserPermission(generics.UpdateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerilizer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['user_id', 'permission_id'],
        ),
        responses={
            200: openapi.Response('Response description', UserPermissionSerilizer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer token',
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        view_name = Endpoint.UPDATE_USER_PERMISSION.value

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
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return response



class GetUserPermission(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated]

    # queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerilizer
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = UserPermission.objects.filter(user_id=user_id)
        return queryset

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', UserPermissionSerilizer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer token',
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        view_name = Endpoint.GET_USER_PERMISSION.value

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
            # lookup_field = 'user_id'
            # instance = self.get_object()
            # serializer = self.serializer_class(instance)
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            
            return JsonResponse(serializer.data, safe=False)
        else:
            return response
        

class DeleteUserPermission(generics.DestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerilizer

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', UserPermissionSerilizer),
            400: "Bad request",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer token',
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        
        view_name = Endpoint.DELETE_USER_PERMISSION.value

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
            instance = self.get_object()
            self.perform_destroy(instance)
            return JsonResponse({'msg': 'deleted'})
        else:
            return response







# class UserPermissionListCreateView(generics.ListCreateAPIView):

#     permission_classes = [permissions.IsAuthenticated]

#     queryset = UserPermission.objects.all()
#     serializer_class = UserPermissionSerilizer

#     @swagger_auto_schema(
#         responses={
#             200: openapi.Response('Response description', UserPermissionSerilizer),
#             400: "Bad request",
#         },
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 description='Bearer token',
#                 type=openapi.TYPE_STRING,
#                 required=True,
#             ),
#         ],
#     )
#     def get(self, request, *args, **kwargs):
#         view_name = Endpoint.USER_PERMISSION.value
#         django_request = HttpRequest()
#         django_request.method = request.method
#         django_request.GET = request.query_params
#         django_request.POST = request.data
#         django_request.user = request.user
#         # Set this attribute to True to disable CSRF checks
#         django_request._dont_enforce_csrf_checks = True

#         middleware = ExampleMiddleware(get_response=self.dispatch)
#         response = middleware(django_request, view_name=view_name)

#         if response.status_code == 200:
#             queryset = self.get_queryset()
#             serializer = self.serializer_class(queryset, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         else:
#             return response

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             },
#             required=['user_id', 'permission_id'],
#         ),
#         responses={
#             201: openapi.Response('Response description', UserPermissionSerilizer),
#             400: "Bad request",
#         },
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 description='Bearer token',
#                 type=openapi.TYPE_STRING,
#                 required=True,
#             ),
#         ],
#     )
#     def post(self, request, *args, **kwargs):
#         view_name = Endpoint.USER_PERMISSION.value

#         django_request = HttpRequest()
#         django_request.method = request.method
#         django_request.GET = request.query_params
#         django_request.POST = request.data
#         django_request.user = request.user
#         # Set this attribute to True to disable CSRF checks
#         django_request._dont_enforce_csrf_checks = True

#         middleware = ExampleMiddleware(get_response=self.dispatch)
#         response = middleware(django_request, view_name=view_name)

#         if response.status_code == 200:
#             serializer = self.serializer_class(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=200)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return response


# class UserPermissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

#     permission_classes = [permissions.IsAuthenticated]

#     queryset = UserPermission.objects.all()
#     serializer_class = UserPermissionSerilizer

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             },
#             required=['user_id', 'permission_id'],
#         ),
#         responses={
#             200: openapi.Response('Response description', UserPermissionSerilizer),
#             400: "Bad request",
#         },
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 description='Bearer token',
#                 type=openapi.TYPE_STRING,
#                 required=True,
#             ),
#         ],
#     )
#     def put(self, request, *args, **kwargs):
#         view_name = Endpoint.USER_PERMISSION_CRUD.value

#         django_request = HttpRequest()
#         django_request.method = request.method
#         django_request.GET = request.query_params
#         django_request.POST = request.data
#         django_request.user = request.user
#         # Set this attribute to True to disable CSRF checks
#         django_request._dont_enforce_csrf_checks = True

#         middleware = ExampleMiddleware(get_response=self.dispatch)
#         response = middleware(django_request, view_name=view_name)

#         if response.status_code == 200:
#             instance = self.get_object()
#             serializer = self.serializer_class(instance, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, safe=False)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return response

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             },
#             required=['user_id', 'permission_id'],
#         ),
#         responses={
#             200: openapi.Response('Response description', UserPermissionSerilizer),
#             400: "Bad request",
#         },
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 description='Bearer token',
#                 type=openapi.TYPE_STRING,
#                 required=True,
#             ),
#         ],
#     )
#     def patch(self, request, *args, **kwargs):
#         view_name = Endpoint.USER_PERMISSION_CRUD.value

#         django_request = HttpRequest()
#         django_request.method = request.method
#         django_request.GET = request.query_params
#         django_request.POST = request.data
#         django_request.user = request.user
#         # Set this attribute to True to disable CSRF checks
#         django_request._dont_enforce_csrf_checks = True

#         middleware = ExampleMiddleware(get_response=self.dispatch)
#         response = middleware(django_request, view_name=view_name)

#         if response.status_code == 200:
#             instance = self.get_object()
#             serializer = self.serializer_class(instance, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, safe=False)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return response

#     @swagger_auto_schema(
#         responses={
#             200: openapi.Response('Response description', UserPermissionSerilizer),
#             400: "Bad request",
#         },
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 description='Bearer token',
#                 type=openapi.TYPE_STRING,
#                 required=True,
#             ),
#         ],
#     )
#     def get(self, request, *args, **kwargs):
#         view_name = Endpoint.USER_PERMISSION_CRUD.value

#         django_request = HttpRequest()
#         django_request.method = request.method
#         django_request.GET = request.query_params
#         django_request.POST = request.data
#         django_request.user = request.user
#         # Set this attribute to True to disable CSRF checks
#         django_request._dont_enforce_csrf_checks = True

#         middleware = ExampleMiddleware(get_response=self.dispatch)
#         response = middleware(django_request, view_name=view_name)

#         if response.status_code == 200:
#             instance = self.get_object()
#             serializer = self.serializer_class(instance)
#             return JsonResponse(serializer.data, safe=False)
#         else:
#             return response

#     @swagger_auto_schema(
#         responses={
#             200: openapi.Response('Response description', UserPermissionSerilizer),
#             400: "Bad request",
#         },
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 description='Bearer token',
#                 type=openapi.TYPE_STRING,
#                 required=True,
#             ),
#         ],
#     )
#     def delete(self, request, *args, **kwargs):
#         view_name = Endpoint.USER_PERMISSION_CRUD.value

#         django_request = HttpRequest()
#         django_request.method = request.method
#         django_request.GET = request.query_params
#         django_request.POST = request.data
#         django_request.user = request.user
#         # Set this attribute to True to disable CSRF checks
#         django_request._dont_enforce_csrf_checks = True

#         middleware = ExampleMiddleware(get_response=self.dispatch)
#         response = middleware(django_request, view_name=view_name)

#         if response.status_code == 200:
#             instance = self.get_object()
#             self.perform_destroy(instance)
#             return JsonResponse({'msg': 'deleted'})
#         else:
#             return response
