from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view,APIView,permission_classes
#imports for serializer
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import ReadOnly  

#this import for pagination
from rest_framework.pagination import PageNumberPagination




'''
#Function based api
@api_view(http_method_names=["GET"])
def post_list(request: Request):

    all_posts=Post.objects.all()

    serializer=PostSerializer(instance=all_posts,many=True)
    response = {
        "message": "all post data fetched successfully",
        "deta": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request: Request, id: int):
    post=get_object_or_404(Post,pk=id)
    serializer=PostSerializer(instance=post)

    if post:
        
        response = {
            "message": f"post Details for id {id} fetched Successfully",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        
        response = {
            "error": f"Post details for id {id} not found"
        }
        return Response(data=response, status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=["POST"])
def post_create(request:Request):
    if request.method == "POST":
        data=request.data
        serializer=PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response={
                "message":"post created successfully",
                "data":serializer.data
            }
    
            return Response(data=response,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_201_CREATED)


@api_view(http_method_names=["PUT"])
def post_update(request:Request,id:int):
    post=get_object_or_404(Post,pk=id)
    data=request.data
    serializer=PostSerializer(instance=post,data=data)
    if serializer.is_valid():
        serializer.save()

        response={
                "message":f"post with id {id} updated successfully",
                "data":serializer.data
            }
        return Response(data=response,status=status.HTTP_200_OK)
    
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def post_delete(request:Request,id:int):
    post=get_object_or_404(Post,pk=id)
    post.delete()
    response={
        "messange":f"post for {id} deleted successfully"
    }
    return Response(data=response,status=status.HTTP_200_OK)
'''
"""
#class based api
class PostsList(APIView):
    def get(self,request:Request,*args,**kwargs):
        posts=Post.objects.all()
        serializer=PostSerializer(instance=posts,many=True)
        response={
            "message":"List os all posts fetched successfully",
            "data":serializer.data
        }

        return Response(data=response,status=status.HTTP_200_OK)


class PostDetail(APIView):
    def get(self,request:Request, id:int):
        post=get_object_or_404(Post,pk=id)
        serializer=PostSerializer(instance=post)

        if post:
            response={
                "message":f"Post details for id{id} fetached successfully ",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)


class PostCreate(APIView):
    def post(self,request:Request,*args,**kwargs):
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"Post created successfully",
                "data":serializer.data
            }

            return Response(data=response,status=status.HTTP_201_CREATED)
        
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class PostUpdate(APIView):
    def put(self,request:Request,id=int):
        post = get_object_or_404(Post,pk = id)
        data = request.data
        serializer = PostSerializer(instance = post,data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
				"message":f"Post with id {id} update successfully",
				"data":serializer.data
			}
            return Response(data = response,status=status.HTTP_200_OK)
        else:
            return Response(data = serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PostDelete(APIView):
    def delete(self,request:Request,id=int):
        post = get_object_or_404(Post,pk=id)
        post.delete()
        response = {
            "message":f"Post id {id} delete successfully"
			}
        return Response(data=response,status=status.HTTP_200_OK)
"""


#genaric api views and model views

#this is just another method of  permission class's 
#@permission_classes([IsAuthenticated])

class CustomPaginator(PageNumberPagination):
    page_size=1
    page_query_param="page"
    page_size_query_param="page_size"


class PostListViews(generics.GenericAPIView,mixins.ListModelMixin):
 
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    pagination_class=CustomPaginator  #this line is use for custom pagination

    def get(self,request:Request):
        return self.list(request)


class PostCreateListViews(generics.GenericAPIView,mixins.CreateModelMixin):

    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def post(self,request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class PostDetailView(generics.GenericAPIView,mixins.RetrieveModelMixin):

    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def get(self,request:Request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class PostUpdateViews(generics.GenericAPIView,mixins.UpdateModelMixin):

    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def put(self,request:Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
class PostDeleteViews(generics.GenericAPIView,mixins.DestroyModelMixin):

    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def delete(self,request:Request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

'''
#viewset and routers-
#viewset base api view-
class PostViewset(viewsets.ViewSet):

    def list(self,request:Request):
        queryset=Post.objects.all()
        serializer=PostSerializer(instance=queryset,many=True)

        response={
            "message":"List of all Post Data Fetched Successfully",
            "data":serializer.data
        }

        return Response(data=response,status=status.HTTP_200_OK)
    
    def retrieve(self,request:Request,pk:None):

'''

