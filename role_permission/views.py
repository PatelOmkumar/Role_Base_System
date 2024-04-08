from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import generics
from django.urls import reverse_lazy
from common.middlewere import ExampleMiddleware
from role_permission.serializers import RolePermissionSerializer
from rest_framework import permissions
from django.utils.encoding import smart_str
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from role_permission.models import RolePermission
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from common.enums import Endpoint
# generate token manually



class GetAllRolePermission(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', RolePermissionSerializer),
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
        view_name = Endpoint.GET_ALL_ROLE_PERMISSION.value

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


class CreateRolePermission(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'role_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['role_id', 'permission_id'],
        ),
        responses={
            201: openapi.Response('Response description', RolePermissionSerializer),
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
        view_name = Endpoint.CREATE_ROLE_PERMISSION.value

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
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return response


class UpdateRolePermission(generics.UpdateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    # queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'role_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['role_id', 'permission_id'],
        ),
        responses={
            200: openapi.Response('Response description', RolePermissionSerializer),
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
        view_name = Endpoint.UPDATE_ROLE_PERMISSION.value

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
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return response


class GetRolePermission(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated]
    # queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
    def get_queryset(self):
        role_id = self.kwargs.get('role_id')
        queryset = RolePermission.objects.filter(role_id=role_id)
        return queryset

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', RolePermissionSerializer),
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
        view_name = Endpoint.GET_ROLE_PERMISSION.value

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
            # instance = self.get_object()
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset,many=True)
            return JsonResponse(serializer.data, status=200, safe=False)
        else:
            return response
        

class DeleteRolePermission(generics.DestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Response description', RolePermissionSerializer),
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
        view_name = Endpoint.DELETE_ROLE_PERMISSION.value

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




# class RolePermissionListCreateView(generics.ListCreateAPIView):

#     permission_classes = [permissions.IsAuthenticated]
#     queryset = RolePermission.objects.all()
#     serializer_class = RolePermissionSerializer

#     @swagger_auto_schema(
#         responses={
#             200: openapi.Response('Response description', RolePermissionSerializer),
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
#         view_name = Endpoint.ROLE_PERMISSION.value

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
#                 'role_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             },
#             required=['role_id', 'permission_id'],
#         ),
#         responses={
#             201: openapi.Response('Response description', RolePermissionSerializer),
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
#         view_name = Endpoint.ROLE_PERMISSION.value

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
#                 return JsonResponse(serializer.data, status=201)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return response


# class RolePermissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

#     permission_classes = [permissions.IsAuthenticated]

#     queryset = RolePermission.objects.all()
#     serializer_class = RolePermissionSerializer

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'role_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             },
#             required=['role_id', 'permission_id'],
#         ),
#         responses={
#             200: openapi.Response('Response description', RolePermissionSerializer),
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
#         view_name = Endpoint.ROLE_PERMISSION_CRUD.value

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
#                 return JsonResponse(serializer.data, status=201)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return response

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'role_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             },
#             required=['role_id', 'permission_id'],
#         ),
#         responses={
#             200: openapi.Response('Response description', RolePermissionSerializer),
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
#         view_name = Endpoint.ROLE_PERMISSION_CRUD.value

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
#                 return JsonResponse(serializer.data, status=200)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return response

#     @swagger_auto_schema(
#         responses={
#             200: openapi.Response('Response description', RolePermissionSerializer),
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
#         view_name = Endpoint.ROLE_PERMISSION_CRUD.value

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
#             return JsonResponse(serializer.data, status=200)
#         else:
#             return response

#     @swagger_auto_schema(
#         responses={
#             200: openapi.Response('Response description', RolePermissionSerializer),
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
#         view_name = Endpoint.ROLE_PERMISSION_CRUD.value

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
