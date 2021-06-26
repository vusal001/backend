from django.utils.translation import activate
from rest_framework import serializers, status
from rest_framework.response import Response 
from post.models import Images, Post
from .serializers import PostSerilaziers, PostImageSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from rest_framework import generics

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .permissions import IsAdminUserOrReadOnly, IsPostUser
from .pagination import Pagination
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

class PostImageView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = PostImageSerializer

    
class PostView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerilaziers

    pagination_class = Pagination

    

    def perform_create(self, serializer):
        serializer.save(post_user=self.request.user)

    filter_backends = [SearchFilter]
    search_fields = ['title', 'text', 'cat']
    # parser_classes = (MultiPartParser, FormParser,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Post.objects.all()
        city = self.request.query_params.get('city')
        ordering= self.request.query_params.get('ordering')

        if city is not None:
            queryset = queryset.filter(city__icontains=city)

        if ordering == 'Tarixe gore':
            queryset = queryset.order_by('posting_date')

        elif ordering == 'Bahadan ucuza':
            queryset = queryset.order_by('price')

        elif ordering == 'Ucuzdan bahaya':
            queryset = queryset.order_by('-price')

        return queryset

    


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilaziers
    permission_classes = [IsPostUser]


    def perform_create(self, serializer):
        serializer.save(post_user=self.request.user)

    
    # def get(self, request, *args, **kwargs):
        # posts = Post.objects.filter(active=True) 
        # serializer = PostSerilaziers(posts, many=True) 
        # return self.list(request, *args, **kwargs)



    # def post(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
        # serializer = PostSerilaziers(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status = status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostDetailView(APIView):

#     def get_object(self, pk):
#         post_instance = get_object_or_404(Post, pk=pk)
#         return post_instance

#     def get(self, request, pk):
#         post = self.get_object(pk=pk)
#         serializer = PostSerilaziers(post)
#         return Response(serializer.data)       

#     def put(self, request, pk):
#         post = self.get_object(pk=pk)
#         serializer = PostSerilaziers(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

#     def delete(self, request, pk):
#         post = self.get_object(pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
















