from django.urls import path
from . import views


"""
#function based api
urlpatterns=[
    path("",views.post_list,name="posts-list"),
    path("<int:id>",views.post_detail,name="post-detail"),
    path("new",views.post_create,name="post_create"),
    path("update/<int:id>",views.post_update,name="post_update"),
    path("delete/<int:id>",views.post_delete,name="post_delete")
]
"""

"""
#class based api
urlpatterns=[
    path("",views.PostsList.as_view(),name="post_list"),
    path("<int:id>",views.PostDetail.as_view(),name="post details"),
    path("new",views.PostCreate.as_view(),name="create post"),
    path("update/<int:id>",views.PostUpdate.as_view(),name="update post"),
    path("delete/<int:id>",views.PostDelete.as_view(),name="delete post"),
]"""




#generic api with mixins
urlpatterns=[
    path("",views.PostListViews.as_view(),name="post_list"),
    path("new",views.PostCreateListViews.as_view(),name="create_post"),
    path("<int:pk>",views.PostDetailView.as_view(),name="post_by_id"),
    path("update/<int:pk>",views.PostUpdateViews.as_view(),name="update_post"),
    path("delete/<int:pk>",views.PostDeleteViews.as_view(),name="delete_post")
] 

