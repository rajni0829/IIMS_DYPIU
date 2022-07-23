from .serializers import ClassroomSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from model_name.models import classroom
from rest_framework.views import APIView



@permission_classes((permissions.AllowAny,))
# def add_product(request):
#     ip = get_client_ip(request)
#     serializer = MyProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(requester_ip=ip)
#     return Response(serializer.data)
class ClassroomList(APIView):
    def get(self,request,status):
        data = classroom.objects.all().filter(status=status)
        serializer=ClassroomSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request,status):
          return Response("in-progress")
          
class FacultyList(APIView):
    def get(self,request,status):
        data = classroom.objects.all().filter(status=status)
        serializer=ClassroomSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request,status):
          return Response("in-progress")
