from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

def redirect_root(request):
    return redirect('blog_post_list')