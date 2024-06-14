from django.urls import path
from user_app.api.views import registration_view, logout_view, login_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #Login utilizando método propio de django rest
    #path ('login/', obtain_auth_token, name='login'),
    
    path ('login-app/', login_view, name='login.app'),
    
    path ('register/', registration_view , name='register'),
    path ('logout/', logout_view , name='logout'),
    
    # path utilizando la librería simpleJWT
    path ('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path ('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]

