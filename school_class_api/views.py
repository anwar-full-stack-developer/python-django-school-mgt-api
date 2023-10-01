from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import SchoolClass
from .serializers import SchoolClassSerializer
from django.shortcuts import get_object_or_404  
  
class SchoolClassView(APIView):  
  
    def get(self, request, id=None):  
        if id:  
            result = SchoolClass.objects.get(id=id)  
            serializers = SchoolClassSerializer(result)  
            return Response({'success': 'success', "data":serializers.data}, status=200)  
  
        result = SchoolClass.objects.all()  
        serializers = SchoolClassSerializer(result, many=True)  
        return Response({'status': 'success', "data":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = SchoolClassSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
  
    def patch(self, request, id):  
        result = SchoolClass.objects.get(id=id)  
        serializer = SchoolClassSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
  
    def delete(self, request, id=None):  
        result = get_object_or_404(SchoolClass, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  