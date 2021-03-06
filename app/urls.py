from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView as TV
from core.views import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("livewire.urls")),
    path('counter', TV.as_view(template_name="counter.html"), name="counter"),
    path('helloworld', TV.as_view(template_name="helloworld.html"),
         name="helloworld"),
    path('posts', posts, name='posts'),
    path('search-posts', TV.as_view(template_name="search_post.html"),
         name="search_post"),
    path('show-posts/', TV.as_view(template_name="show_post.html"),
         name="show_post"),
    path('register', TV.as_view(template_name="register.html")),
    path('', TV.as_view(template_name="index.html"), name="index"),
] + staticfiles_urlpatterns()
