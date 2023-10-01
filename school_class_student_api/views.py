from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import SchoolClassStudent
from .serializers import SchoolClassStudentSerializer  
from django.shortcuts import get_object_or_404  
  
class SchoolClassStudentView(APIView):  
  
    def get(self, request, id=None):  
        if id:  
            result = SchoolClassStudent.objects.get(id=id)  
            serializers = SchoolClassStudentSerializer(result)  
            return Response({'success': 'success', "data":serializers.data}, status=200)  
  
        result = SchoolClassStudent.objects.all()  
        serializers = SchoolClassStudentSerializer(result, many=True)  
        return Response({'status': 'success', "data":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = SchoolClassStudentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
  
    def patch(self, request, id):  
        result = SchoolClassStudent.objects.get(id=id)  
        serializer = SchoolClassStudentSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
  
    def delete(self, request, id=None):  
        result = get_object_or_404(SchoolClassStudent, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  