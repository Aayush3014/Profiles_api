from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from .serializers import UserProfileSerializer
from .models import UserProfile
from api import permissions

# class CrudApi(APIView):
    
#     serializer_class = HelloSerialier
    
#     def get(self, request, format=None):
#         """Returns a list of all the data in APIView."""
        
#         api = [
#             'uses HTTP',
#             'is mapped manualy to urls',
#         ]
        
#         return Response({'msg':'hello','api':api})
        
        
#     def post(self,request,format=None):
#         """Create a hello message with our name."""
        
#         serializer = self.serializer_class(data=request.data)
        
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'hello {name}'
            
#             return Response({'message':message})
#         return Response(serializer.errors)


class UserProfileViewSet(viewsets.ModelViewSet):
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ['email','name']