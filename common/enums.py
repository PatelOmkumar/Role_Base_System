from enum import Enum

class Endpoint(Enum):
    
    CREATE_ROLES= 'create_role/'
    GET_ROLE = 'get_role/<int:pk>/'
    GET_ALL_ROLE = 'get_all_role/'
    UPDATE_ROLE = 'update_role/<int:pk>/'
    DELETE_ROLE = 'delete_role/<int:pk>/'


    GET_ALL_PERMISSION = 'get_all_permission/'
    GET_PERMISSION = 'get_permission/<int:pk>/'
    CREATE_PERMISSION = 'create_permission/'
    UPDATE_PERMISSION = 'update_permission/<int:pk>/'
    DELETE_PERMISSION = 'delete_permission/<int:pk>/'


    CREATE_ROLE_PERMISSION = 'create_rolepermission/'
    GET_ROLE_PERMISSION = 'get_rolepermission/<int:pk>/'
    GET_ALL_ROLE_PERMISSION = 'get_all_rolepermission/'
    UPDATE_ROLE_PERMISSION = 'update_rolepermission/<int:pk>/'
    DELETE_ROLE_PERMISSION = 'delete_rolepermission/<int:pk>/'

    GET_ALL_USER_PERMISSION = 'get_all_userpermission/'
    GET_USER_PERMISSION = 'get_userpermission/<int:pk>/'
    UPDATE_USER_PERMISSION = 'update_userpermission/<int:pk>/'
    CREATE_USER_PERMISSION = 'create_userpermission/'
    DELETE_USER_PERMISSION = 'delete_userpermission/<int:pk>/'

    DATA_VIEW = 'dataview/'
    ALL_USER_DATA_VIEW = 'alluserdataview/'
    USER_UPDATE_DETAILS = 'userupdatedetails/'
    CHANGE_PASSWORD = 'changepassword/'
    SEND_RESET_PASSWORD_EMAIL = 'send-reset-password-email/'
    RESET_PASSWORD = 'reset-password/'
    USER_DELETE = 'userdelete/'