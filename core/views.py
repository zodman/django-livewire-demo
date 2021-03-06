from django.shortcuts import render
from livewire.views import LivewireComponent
from django.db.models import Q
from core.models import Post
import logging

log = logging.getLogger(__name__)


def posts(request):
    context = {
        'posts': list(Post.objects.all().values("id", "title", "content"))
     }
    return render(request, "posts.html", context)


class PostsLivewire(LivewireComponent):
    template_name = "posts.livewire.html"
    def mount(self, **kwargs):
        posts = kwargs.get("posts")
        return {
            'posts': posts
        }


class CounterLivewire(LivewireComponent):
    template_name="counter.livewire.html"
    count = 2

    def decrement(self, *args):
        self.count -= 1

    def increment(self, *args):
        self.count += 1



class HelloworldLivewire(LivewireComponent):
    template_name = "helloworld.livewire.html"
    message = "Hellowwwww mundo!"


class HelloworldDatabindLivewire(LivewireComponent):
    template_name = "helloworld_databind.livewire.html"
    message = "Hellowwwww mundo!"


class SearchPostsLivewire(LivewireComponent):
    template_name="search_posts.livewire.html"
    search = ""
    updates_query_string = ("search", )
    # TODO must recive the request
    def mount(self, **kwargs):
        posts = Post.objects.all()
        if self.search:
            param = Q(title__icontains=self.search) | Q(content__icontains=self.search)
            posts = posts.filter(param)
        return {
            'posts': list(posts.values("id", "title", "content")),
        }


class ShowPostLivewire(LivewireComponent):
    post_id = None


    def mount(self, **kwargs):
        post_id = kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        self.post_id = post_id
        return {
            'post': {'title': post.title, 'content': post.content}
        }



