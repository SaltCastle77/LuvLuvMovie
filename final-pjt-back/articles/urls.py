from django.urls import path
from . import views

urlpatterns = [
    #articles/
    path('',views.article_list_create),
    path('<int:article_pk>/',views.article_detail_update_delete),
    path('<int:article_pk>/comments/',views.create_comment),
    path('comments/', views.comment_list),
    path('<int:article_pk>/comments/<int:comment_pk>/',views.comment_delete_update)
]