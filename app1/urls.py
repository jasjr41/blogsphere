from . import views
from django.urls import path
urlpatterns = [
    path('blogs/', views.blogs),
    path("", views.home),
    path("create/", views.create_blog, name="create"),
    path("blogs/<slug:blog>", views.blog_types, name="blog_types"),
    path('<path:undefined_path>/', views.custom_404)

]