from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from django.http import Http404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings

#Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

from rest_framework.permissions import IsAuthenticated
from crudeappangular.models import Userdata
from crudeappangular.serializers import UserSerializer,TokenSerializer




class CrudeOperation(APIView):

    def get(self,request):
         print("get")
         if request.method=='GET':
            try:
                data = Userdata.objects.all()
                serializer = UserSerializer(data,many=True)
                return Response({'status':serializer.data})
            except Exception as e:

                return Response({'status:':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def post(self,request,format=None):
         permission_classes = [IsAuthenticated] 
         if request.method=='POST':
            print("hello",request.data)
            try:
                serializer = UserSerializer(data=request.data)
                #print("user",serializer.data)
                if serializer.is_valid():
                    print("hello saving data")
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'status:':serializer.errors},status=status.HTTP_400_BAD_REQUEST)




    def put(self,request):
        if request.method=='PUT':
            try:
                print("id",request.data['id'])
                data = Userdata.objects.get(id=request.data['id'])
                serializer = UserSerializer(data, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                    print("put method")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print("error")
                return Response({'error' : str(e)},status=500)



    def delete(self,request):
        if request.method=='DELETE':
            
            try:
                snippet = Userdata.objects.get(id=request.data['id'])
                snippet.delete()
                return Response({'status':"ok delete"}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({'status:':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterUsers(APIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print("ddd",request.data.get("username", ""))
        try:
            username = request.data.get("username", "")
            password = request.data.get("password", "")
            email = request.data.get("email", "")
            if not username and not password and not email:
                return Response(
                    data={
                        "message": "username, password and email is required to register a user"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            new_user = User.objects.create(
                username=username, password=password, email=email
            )
            return Response({"message":"registered"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class LoginView(APIView):
    """
    POST auth/login/
    
    This permission class will overide the global permission
    class setting
    """
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get("username", "")
            password = request.data.get("password", "")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # login saves the user’s ID in the session,
                # using Django’s session framework.
                login(request, user)
                serializer = TokenSerializer(data={
                    # using drf jwt utility functions to generate a token
                    "token": jwt_encode_handler(
                        jwt_payload_handler(user)
                    )})
                serializer.is_valid()
                return Response({"data":serializer.data})
            return Response({"msg":"user does not exist"},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)