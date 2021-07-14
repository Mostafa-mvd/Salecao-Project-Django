from django.shortcuts import render
from blog.models import Post
from services.models import OurServices

# Create your views here.


def startup_page(request):
    services_items = OurServices.objects.all()
    random_posts = Post.objects.order_by("?")[0:3]
    context = {"random_posts": random_posts, "services": services_items}
    return render(request, "main.html", context)
