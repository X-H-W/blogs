from django.shortcuts import render
from .models import Banner
from .models import Post
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index(request):
    banner_list = Banner.objects.all()
    post_list = Post.objects.filter(is_recomment=True)

    ctx = {
        'banner_list': banner_list,
        'post_list': post_list
    }
    return render(request, 'index.html', ctx)


def blog_list(request):
    post_list = Post.objects.all()

    try:
        page = request.GET.get('page', 1)

    except PageNotAnInteger:
        page = 1
    p = Paginator(post_list, per_page=1, request=request)
    post_list = p.page(page)
    ctx = {
     'post_list': post_list,
    }
    return render(request, 'list.html', ctx)

