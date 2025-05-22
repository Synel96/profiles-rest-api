from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets 

class HelloApiView(APIView):
    """"Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = ["Uses HTTP methods as function (get,post,patch,put,delete)",
        "Is similar to a tradtional DjangoView",
        "Gives you the most control over application logic ",
        " is mapped manually URLs"]

        return Response({"message" : "Hello", "an_apiview" : an_apiview})
    
    def post(self,request):
        """Create a hello message from our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")

            message = f"Hello {name}"

            return Response({"message" : message} )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def put(self,request,pk=None):
        """Handle updating an object"""

        return Response({"method" : "put"})
    
    def patch(self, request, pk=None):
        "Handle partial update of an opbject"

        return Response({"method" : "PATCH" })
    
    def delete(self, request, pk=None):
        """Deleting an object"""

        return Response({"method": "DELETE"})
    

class HelloViewSets(viewsets.ViewSet):
    """Test API ViewSets"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""

        a_viewset = [
            "uses actions (list,retrive,update,partial_update)",
            "automatically maps to URLs using routers",
            "proives more funcitonality with less code",

        ]

        return Response({"message" :"Hello ", "a_viewset" : a_viewset})
    

    def create(self,request):
        """Create a new Hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"

            return Response({"message": message})
        
        else :
            return Response (
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

    def retrive(self,request, pk=None):
        """Handle getting an object by its ID"""

        return Response({"HTTP method" : "GET"})
    
    def update(self,request, pk=None):
        """Handle updating an object"""

        return Response({"HTTP method " : "PUT"})
    
    def partial_update(self,request, pk=None):
        """Handle updating part of an object"""

        return Response({"HTTP method" : "PATCH"})
    
    def destroy(self,request, pk=None):
        """Handle removing an object"""

        return Response({"HTTP method" : "DELETE"})