from django.urls import path
from .import views

app_name='post'
urlpatterns = [
  path('create/',views.create_view,name='create_view'),
  path('detail/<post_id>', views.post_detail_view, name='post_detail_view'),
  path('update/<post_id>', views.post_update_view, name="post_update_view"),
  path('delete/<post_id>', views.post_delete_view, name="post_delete_view"),
  path('all/', views.all_post_view, name='all_post_view'),
  path('search/', views.search_post_view, name="search_post_view")

]
