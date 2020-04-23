from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post

class PostList(View):
    template_name='blog/post_list.html'
    def get(self, request):
        return render(request,self.template_name,{'post_list':Post.objects.all()})

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year = year, pub_date__month =month, slug__iexact=slug)
    return render( request, 'blog/post_detail.html', {'post':post})