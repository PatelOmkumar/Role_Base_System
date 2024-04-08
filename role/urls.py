from django.urls import path
from role.views import GetAllRole,GetRole,UpdateRole,DeleteRole,CreateRole

urlpatterns = [
    path('get_all_role/', GetAllRole.as_view(), name="get_all_role"),
    path('create_role/', CreateRole.as_view(), name="create_role"),
    path('get_role/<int:pk>/',
         GetRole.as_view(), name="get_role"),
    path('update_role/<int:pk>/',
         UpdateRole.as_view(), name="update_role"),
    path('delete_role/<int:pk>/',
         DeleteRole.as_view(), name="delete_role")

]
