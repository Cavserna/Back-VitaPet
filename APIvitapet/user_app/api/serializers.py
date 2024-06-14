from rest_framework import serializers
from user_app.models import Account


# serializer que modela el registro de usuario

class RegistrationSerializer(serializers.ModelSerializer):
    # Incluir un password2 como campo calculado desde el serializer al modelo User de Django
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'phone_number']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
     
    # mètodo para generar el modelo serializador para registrar un usuario    
    def save(self):
        # Capturar los datos que se necesitan para validar
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
            
        # Validar si el password2 coincide con el password
        if password != password2:
            raise serializers.ValidationError({ 'error': 'Las contraseñas no coinciden'})
            
        # Validar si un usuario ya tiene su correo registrado
        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({ 'error': 'El email ya está registrado'})
            
        account = Account.objects.create_user(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            password = self.validated_data['password'],
        )
        account.set_password = self.validated_data['password']
        account.phone_number = self.validated_data['phone_number']
    
        account.save()
        return account
    