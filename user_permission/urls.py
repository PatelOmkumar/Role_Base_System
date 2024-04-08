from django.urls import path
from user_permission.views import GetAllUserPermission,CreateUserPermission,UpdateUserPermission,GetUserPermission,DeleteUserPermission
urlpatterns = [
    path('get_all_userpermission/', GetAllUserPermission.as_view(),
         name="get_all_userpermission"),
    path('create_userpermission/', CreateUserPermission.as_view(),
         name="create_userpermission"),
    path('get_userpermission/<int:user_id>/', GetUserPermission.as_view(),
         name="get_userpermission"),
    path('update_userpermission/<int:pk>/', UpdateUserPermission.as_view(),
         name="update_userpermission"),
    path('delete_userpermission/<int:pk>/', DeleteUserPermission.as_view(),
         name="delete_userpermission"),

]
