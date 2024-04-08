from django.urls import path
from authentication_module.views import UserRegistrationView, VerifyEmailView, UserLoginView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordRestView,UserDataView, AllUserDataView, UserUpdateDetailsView, UserDeleteView




urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name="signup"),
    path('verify_email/<uidb64>/<token>/', VerifyEmailView.as_view(), name="verify_email"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('change_password/', UserChangePasswordView.as_view(),
         name="change_password"),
    path('send_reset_password_email', SendPasswordResetEmailView.as_view(),
         name="send_reset_password_email"),
    path("user_reset_password/<uid>/<token>/",
         UserPasswordRestView.as_view(), name="user_reset_password"),
     path('all_user_data/', AllUserDataView.as_view(), name="all_user_data"),
    path("user_data/", UserDataView.as_view(), name="user_data"),
    path('user_update/', UserUpdateDetailsView.as_view(), name="user_update"),
    path('user_delete', UserDeleteView.as_view(), name="user_delete"),
]

