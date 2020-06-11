from django.shortcuts import render, get_object_or_404
from .models import ImagePost, VideoPost, YoutubePost
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# Text Posts
def index(request):
    infoCarousel = ImagePost.objects.order_by('date')
    infoImage = ImagePost.objects.order_by('date')
    infoVideo = VideoPost.objects.all
    infoYoutube = YoutubePost.objects.all
    paginator = Paginator(infoImage, 6)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'infoCarousel':infoCarousel,
        'posts': posts,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,

    }
    return render(request, 'appBlogd/index.html', context)


def categoryBusiness(request):
    infoImage = ImagePost.objects.filter(category__contains="business")
    infoVideo = VideoPost.objects.filter(category__contains="business")
    infoYoutube = YoutubePost.objects.filter(category__contains="business")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryCar(request):
    infoImage = ImagePost.objects.filter(category__contains="cars")
    infoVideo = VideoPost.objects.filter(category__contains="cars")
    infoYoutube = YoutubePost.objects.filter(category__contains="cars")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


# Category Viewing Functions
def categoryCelebrity(request):
    infoImage = ImagePost.objects.filter(category__contains="celebrity")
    infoVideo = VideoPost.objects.filter(category__contains="celebrity")
    infoYoutube = YoutubePost.objects.filter(category__contains="celebrity")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryHistory(request):
    infoImage = ImagePost.objects.filter(category__contains="history")
    infoVideo = VideoPost.objects.filter(category__contains="history")
    infoYoutube = YoutubePost.objects.filter(category__contains="history")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryLifestyle(request):
    infoImage = ImagePost.objects.filter(category__contains="lifestyle")
    infoVideo = VideoPost.objects.filter(category__contains="lifestyle")
    infoYoutube = YoutubePost.objects.filter(category__contains="lifestyle")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryMatatu(request):
    infoImage = ImagePost.objects.filter(category__contains="matatu culture")
    infoVideo = VideoPost.objects.filter(category__contains="matatu culture")
    infoYoutube = YoutubePost.objects.filter(category__contains="matatu culture")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryMemes(request):
    infoImage = ImagePost.objects.filter(category__contains="memes and vines")
    infoVideo = VideoPost.objects.filter(category__contains="memes and vines")
    infoYoutube = YoutubePost.objects.filter(category__contains="memes and vines")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryReviews(request):
    infoImage = ImagePost.objects.filter(category__contains="music and series review")
    infoVideo = VideoPost.objects.filter(category__contains="music and series review")
    infoYoutube = YoutubePost.objects.filter(category__contains="music and series review")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryPolitics(request):
    infoImage = ImagePost.objects.filter(category__contains="politics")
    infoVideo = VideoPost.objects.filter(category__contains="politics")
    infoYoutube = YoutubePost.objects.filter(category__contains="politics")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categorySports(request):
    infoImage = ImagePost.objects.filter(category__contains="sports")
    infoVideo = VideoPost.objects.filter(category__contains="sports")
    infoYoutube = YoutubePost.objects.filter(category__contains="sports")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryTechnology(request):
    infoImage = ImagePost.objects.filter(category__contains="technology")
    infoVideo = VideoPost.objects.filter(category__contains="technology")
    infoYoutube = YoutubePost.objects.filter(category__contains="technology")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryYouths(request):
    infoImage = ImagePost.objects.filter(category__contains="youths corner")
    infoVideo = VideoPost.objects.filter(category__contains="youths corner")
    infoYoutube = YoutubePost.objects.filter(category__contains="youths corner")
    context = {
        'infoImage': infoImage,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,
    }
    return render(request, 'appBlogd/category.html', context)


# View Image Post Function
def viewImage_post(request, view_id):
    result = get_object_or_404(ImagePost, pk=view_id)
    context = {
        'result': result,
    }
    return render(request, 'appBlogd/viewImage_post.html', context)


# View Video Post Function
def viewVideo_post(request, view_id):
    result = get_object_or_404(VideoPost, pk=view_id)
    context = {
        'result': result,
    }
    return render(request, 'appBlogd/viewVideo_post.html', context)


# View Video Post Function
def viewYoutube_post(request, view_id):
    result = get_object_or_404(YoutubePost, pk=view_id)
    context = {
        'result': result,
    }
    return render(request, 'appBlogd/viewYoutube_post.html', context)