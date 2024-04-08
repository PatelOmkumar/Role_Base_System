from django.urls import path
from role_permission.views import CreateRolePermission,GetAllRolePermission,GetRolePermission,UpdateRolePermission,DeleteRolePermission

urlpatterns = [
    path('get_all_rolepermission/', GetAllRolePermission.as_view(),
         name="get_all_rolepermission"),
    path('create_rolepermission/', CreateRolePermission.as_view(),
         name="create_rolepermission"),
    path('get_rolepermission/<int:role_id>/', GetRolePermission.as_view(),
         name="get_rolepermission"),
    path('update_rolepermission/<int:pk>/', UpdateRolePermission.as_view(),
         name="update_rolepermission"),
    path('delete_rolepermission/<int:pk>/', DeleteRolePermission.as_view(),
         name="delete_rolepermission"),

]
