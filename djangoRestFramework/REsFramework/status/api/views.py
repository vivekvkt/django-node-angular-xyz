import json
from rest_framework import generics, mixins
#from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from status.models import Status
from .serializers import StatusSerializers


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

#CreateModelMixin -- post data
#updateModelMixin ---   put data 
class GenericStatusLisAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.ListAPIView
    ):
    
    permission_classes = []
    authentication_classes = []
    #queryset               = Status.objects.all()
    serializer_class       = StatusSerializers
    
    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains= query)
        return qs
    
    def get_object(self):
        request = self.request
        passed_id = self.request.GET.get('id', None)
        # queryset  = self.queryset()
        queryset  = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset,id=passed_id)
            self.check_object_permissions(request,obj)
        return obj
    
    """ overide method"""
    def get(self, request, *args, **kwargs):
        url_passed_id   = self.request.GET.get('id', None)
        json_data       = {}
        body_           = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None
        
        if  passed_id is not None:
            return self.retrieve(request,*args, **kwargs)
        return super().get(request,*args,**kwargs)
    
    
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
        
    def put(self, request,*args,**kwargs):
        return self.update(request, *args,**kwargs)
    
    def patch(self, request,*args,**kwargs):
        return self.update(request, *args,**kwargs)
    
    def delete(self, request,*args,**kwargs):
        return self.destroy(request, *args,**kwargs)





# class StatusListSerachAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
    
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializers(qs,many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializers(qs,many=True)
#         return Response(serializer.data)
    
   
   
# #CreateModelMixin -- post data
# #updateModelMixin ---   put data 
# class GenericStatusLisAPIView(mixins.CreateModelMixin,generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     #queryset               = Status.objects.all()
#     serializer_class       = StatusSerializers
    
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains= query)
#         return qs
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
    
# # class GenericStatusCreateAPIView(generics.CreateAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset               = Status.objects.all()
# #     serializer_class       = StatusSerializers
    

# class GenericStatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset               = Status.objects.all()
#     serializer_class       = StatusSerializers
    

# class GenericStatusDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset               = Status.objects.all()
#     serializer_class       = StatusSerializers
    
    
    
#     def put(self, request,*args,**kwargs):
#         return self.update(request, *args,**kwargs)
    
#     def patch(self, request,*args,**kwargs):
#         return self.update(request, *args,**kwargs)
    
#     def delete(self, request,*args,**kwargs):
#         return self.destroy(request, *args,**kwargs)
    
    
    
    
    
    
# class GenericStatusDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset               = Status.objects.all()
#     serializer_class       = StatusSerializers
    # lookup_field           ='id'
    
    # def get_object(self , *args,**kwargs):
    #     kwargs = self.kwargs
    #     kwargs_id = kwargs.get('id')
    #     return Status.objects.get(id=kwargs_id)
    

# class GenericStatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset               = Status.objects.all()
#     serializer_class       = StatusSerializers
    
    
# class GenericStatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset               = Status.objects.all()
#     serializer_class       = StatusSerializers
        
        
   