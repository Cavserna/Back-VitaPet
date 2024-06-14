from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth


# mètodo view para eliminar un token y generar un logout
@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# método view que se encarga de procesar la creación de un usuario. Llama al serializer que contiene la logica de serilizar la data y disparar eventos de validación
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        # Se crea un objeto de tipo serializer con la data que envía el usuario. Ojo: es un deserializer porque convierte un objeto json a datos complejos
        serializer = RegistrationSerializer(data=request.data)
        # Este diccionario se va a ir llenado dependiendo de las condiciones
        data={}
        
        # Se valida que el objeto serializer sea valido, aquí hace las validaciones que dejamos en el Registrationserializer
        if serializer.is_valid():
            # una vez validado hace un serializer.save para enviarlo a la bd y ademas queda capturada la intancia en la varianle account
            account = serializer.save()
            # Llenar la variable data con propiedades (properties) y mensajes para cada una
            data ['response'] = 'El registro del usuario fue exitoso'
            data ['username'] = account.username
            data ['email'] = account.email
            data ['first_name'] = account.first_name
            data ['last_name'] = account.last_name
            data ['phone_number'] = account.phone_number
            
            # carga el token en una variable para poder ser cargada en el diccionario data
            # token = Token.objects.get(user=account).key
            # data ['token'] = token
            
            # Utiliza refreshToken de la librería simple JWT para generar el token
            refresh = RefreshToken.for_user(account)
            data ['token'] = {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token)
            }
        else:
            data = serializer.errors
            
        return Response (data) 
  
#View para crear el login de un usuario  
@api_view(['POST']) 
def login_view(request):
    data = {}
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
    # Se validan los datos enviados por el usuario    
        account = auth.authenticate(email = email, password=password)
            
        if account is not None:
            data['Response'] = 'El logín fue exitoso' 
            data['username'] = account.username 
            data['email'] = account.email 
            data['first_name'] = account.first_name 
            data['last_name'] = account.last_name   
            data['phone_number'] = account.phone_number
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            } 
            return Response (data)
        else:
            data ['Error'] = 'Credenciales incorrectas', 
            return Response (data, status.HTTP_500_INTERNAL_SERVER_ERROR)    