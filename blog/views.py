from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Post
from .forms import commentform

# Create your views here.
all_posts = []

class startingPage(ListView):
    template_name ="blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name="posts"

    def get_queryset(self):
       queryset= super().get_queryset()
       data = queryset[:3]
       return data
   
    
    
# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })


class AllPosts(ListView):
    template_name ="blog/all-posts.html"
    model = Post
    context_object_name ="all_posts"


def post_details(request, slug):
    identify_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identify_post,
        "post_tags": identify_post.tags.all()
    })
# class SinglePost(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         context["comment_tags"]=commentform()
#         return context
    
        

class SinglePost(View):
    def is_store(self,request,post_id):
        store_posts = request.session.get("store_posts")
        if store_posts is not None:
            is_later = post_id in store_posts
        else:
            is_later = False

        return is_later
       
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags":post.tags.all(),
            "comment_tags":commentform(),
            "post_comments":post.comments.all().order_by("-id"),
            "store_post":self.is_store(request,post.id)
        }
        return render(request,"blog/post-detail.html",context)
    def post(self,request,slug):
        comment_form = commentform(request.POST)
        post = Post.objects.get(slug=slug) 

        if comment_form.is_valid():
            comments =comment_form.save(commit=False)
            comments.post = post
            comments.save()
            return HttpResponseRedirect(reverse("post_details", args=[slug]))
       
        context ={
            "post":post,
            "post_tags":post.tags.all(),
            "comment_tags":comment_form,
            "post_comments":post.comments.all().order_by("-id"),
            "store_post":self.is_store(request,post.id)
        }
        return render(request,"blog/post-detail.html",context)


class ReadLaterView(View):

    def get(self,request):
        store_posts = request.session.get("store_posts")

        context={}

        if store_posts is None or len(store_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            context["posts"]= Post.objects.filter(id__in=store_posts)
            context["has_posts"]=True    

        return render(request,"blog/stored_post.html",context)

    def post(self,request):
        store_posts = request.session.get("store_posts")

        if store_posts is None:
            store_posts=[]

        post_id = int(request.POST["post_id"])

        if post_id not in store_posts:
            store_posts.append(post_id)
        else:
            store_posts.remove(post_id)
        request.session["store_posts"] = store_posts         
            
             
        return HttpResponseRedirect("/")  


