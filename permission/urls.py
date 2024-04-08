from django.urls import path
from permission.views import GetAllPermission,CreatePermission,GetPermission,DeletePermission,UpdatePermission

urlpatterns = [
    path('get_all_permission/',GetAllPermission.as_view(),name="get_all_permission"),
    path('create_permission/',CreatePermission.as_view(),name="create_permission"),
    path("get_permission/<int:pk>/",GetPermission.as_view(),name="get_permission"),
    path("update_permission/<int:pk>/",UpdatePermission.as_view(),name="update_permission"),
    path("delete_permission/<int:pk>/",DeletePermission.as_view(),name="delete_permission"),

]
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMDcwMjUxLCJpYXQiOjE3MTIwNTgyNTEsImp0aSI6IjFlODQyMTBlOWNhYTQ2MjU5YjhkYjQ3MzUwZmRlYTBlIiwidXNlcl9pZCI6MX0.8vywGfxuGVZ2wXABUpAnaIApnC0kJye8z-bfwH2Sq2k
