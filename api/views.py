from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from .permissions import StudentPermission, StudentDetailPermission, TeacherPermission, TeacherDetailPermission, StudyCenterPermission, StudyCenterDetailPermission
from app.models import Teacher, StudyCenter, Student
from .serializers import TeacherSerializer, StudyCenterSerializer, StudentSerializer

@api_view(['GET', 'POST'])
@permission_classes([StudentPermission])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([StudentDetailPermission])
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)
"""------------------------------------------------------------------------------------------------"""

@api_view(['GET', 'POST'])
@permission_classes([TeacherPermission])
def teacher(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TeacherDetailPermission])
def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=HTTP_204_NO_CONTENT)
"""------------------------------------------------------------------------------------------------"""
@api_view(['GET', 'POST'])
@permission_classes([StudyCenterPermission])
def study_center(request):
    if request.method == 'GET':
        study_centers = StudyCenter.objects.all()
        serializer = StudyCenterSerializer(study_centers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudyCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([StudyCenterDetailPermission])
def study_center_detail(request, pk):
    study_center = StudyCenter.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StudyCenterSerializer(study_center)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudyCenterSerializer(study_center, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        study_center.delete()
        return Response(status=HTTP_204_NO_CONTENT)