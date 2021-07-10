from django.urls import path


from .views import *


urlpatterns = [
    path('', index, name='receipts_list_urls'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name="post_delete_url"),
    path('categories/', posts_list, name='categories'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('categories/<int:dish_id>/', show_dish, name='viewDish'),
    path('reviews/', show_reviews, name='review'),
]
