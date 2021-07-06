from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.generics import  GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin


# Generic APIView and Model Mixins combined code
# List and Create - PK are not required
class StudentLC(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # list the objects
    def get(self, request,  *args, **kwargs):    
        return self.list(request, *args, **kwargs)
    # post/create the objects
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# Retrieve, Update and Delete objects - PK required
class StudentRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Retrieve Data
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # Update Data
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # Destroy Data
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





# Generic APIView and Model Mixins
# # List Student Data
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self, request,  *args, **kwargs):    
#         return self.list(request, *args, **kwargs)
# # Create Student
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# # Retrive Student Data
# class StudentRetrive(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# # Update Student Data
# class StudentUpdate(UpdateAPIView, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# # Destroy data
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# # Class Based Api_View
# class StudentAPI(APIView):
#     def get(self, request, pk = None ,format = None):
#         if request.method == 'GET':
#         # id = request.data.get('id')
#             id = pk
#             if id is not None:
#                 stu = Student.objects.get(pk = id)
#                 serializer = StudentSerializer(stu)
#                 return Response(serializer.data)
#             else:
#                 stu = Student.objects.all()
#                 serializer = StudentSerializer(stu, many = True)
#                 return Response(serializer.data)
    
#     def post(self, request,format = None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Successful Created'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk = None ,format = None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk = id)
#             serializer = StudentSerializer(stu, data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'Complete Data Successful Updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk = None ,format = None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk = id)
#             serializer = StudentSerializer(stu, data = request.data, partial = True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'Partial Data Successful Updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk = None ,format = None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response({'msg': 'Successful Deleted'}, status=status.HTTP_200_OK)






# Create your views here.
# Function Based Api_View
# from rest_framework.decorators import api_view
# @api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
# def student_api(request, pk = None):
#     if request.method == 'GET':
#         # id = request.data.get('id')
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         else:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many = True)
#             return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Successful Created'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':
#         # id = request.data.get('id')
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk = id)
#             serializer = StudentSerializer(stu, data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'Complete Data Successful Updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         # id = request.data.get('id')
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk = id)
#             serializer = StudentSerializer(stu, data = request.data, partial = True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'Partial Data Successful Updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response({'msg': 'Successful Deleted'}, status=status.HTTP_200_OK)

    
