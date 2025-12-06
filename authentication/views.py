from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class UserRegisterView(APIView):
    def post(self, request):
        print("=====REQUEST DATA=====> ", request.data)
        
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=email).exists():
            return Response({"message": "user already exists"}, status=status.HTTP_200_OK)

        try:
            created = User.objects.create_user(
                username=email,  
                email=email, 
                password=password 
            )
            return Response(
                {"message": "account created successfully. login now", "username": created.username},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)