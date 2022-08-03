from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied



class AuthenticationService:
    def base_authencation(self, request):
        email = request.data['email']
        password = request.data['password']

        if email and password:
            user = authenticate(request=request,email=email, password=password)
            if not user:
                 raise PermissionDenied
        else:
            raise PermissionDenied
        
        login(request=request, user=user) 
    
    def logout_user(self, request):
        logout(request)
