from django.shortcuts import render, get_object_or_404
from .models import ImagePost, VideoPost, YoutubePost
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# Text Posts
def index(request):
    infoCarousel = ImagePost.objects.order_by('?')
    infoImage = ImagePost.objects.order_by('?')
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
        'infoCarousel': infoCarousel,
        'posts': posts,
        'infoVideo': infoVideo,
        'infoYoutube': infoYoutube,

    }
    return render(request, 'appBlogd/index.html', context)


# Category Viewing Functions
def categoryBusiness(request):
    infoImage = ImagePost.objects.filter(category__contains="business")
    imageCount = ImagePost.objects.filter(category__contains="business").count()
    infoVideo = VideoPost.objects.filter(category__contains="business")
    videoCount = VideoPost.objects.filter(category__contains="business").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="business")
    youtubeCount = YoutubePost.objects.filter(category__contains="business").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)

def categoryCar(request):
    infoImage = ImagePost.objects.filter(category__contains="cars")
    imageCount = ImagePost.objects.filter(category__contains="cars").count()
    infoVideo = VideoPost.objects.filter(category__contains="cars")
    videoCount = VideoPost.objects.filter(category__contains="cars").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="cars")
    youtubeCount = YoutubePost.objects.filter(category__contains="cars").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryCelebrity(request):
    infoImage = ImagePost.objects.filter(category__contains="celebrity")
    imageCount = ImagePost.objects.filter(category__contains="celebrity").count()
    infoVideo = VideoPost.objects.filter(category__contains="celebrity")
    videoCount = VideoPost.objects.filter(category__contains="celebrity").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="celebrity")
    youtubeCount = YoutubePost.objects.filter(category__contains="celebrity").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryHistory(request):
    infoImage = ImagePost.objects.filter(category__contains="history")
    imageCount = ImagePost.objects.filter(category__contains="history").count()
    infoVideo = VideoPost.objects.filter(category__contains="history")
    videoCount = VideoPost.objects.filter(category__contains="history").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="history")
    youtubeCount = YoutubePost.objects.filter(category__contains="history").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryLifestyle(request):
    infoImage = ImagePost.objects.filter(category__contains="lifestyle")
    imageCount = ImagePost.objects.filter(category__contains="lifestyle").count()
    infoVideo = VideoPost.objects.filter(category__contains="lifestyle")
    videoCount = VideoPost.objects.filter(category__contains="lifestyle").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="lifestyle")
    youtubeCount = YoutubePost.objects.filter(category__contains="lifestyle").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryMatatu(request):
    infoImage = ImagePost.objects.filter(category__contains="matatu culture")
    imageCount = ImagePost.objects.filter(category__contains="matatu culture").count()
    infoVideo = VideoPost.objects.filter(category__contains="matatu culture")
    videoCount = VideoPost.objects.filter(category__contains="matatu culture").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="matatu culture")
    youtubeCount = YoutubePost.objects.filter(category__contains="matatu culture").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryMemes(request):
    infoImage = ImagePost.objects.filter(category__contains="memes and vines")
    imageCount = ImagePost.objects.filter(category__contains="memes and vines").count()
    infoVideo = VideoPost.objects.filter(category__contains="memes and vines")
    videoCount = VideoPost.objects.filter(category__contains="memes and vines").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="memes and vines")
    youtubeCount = YoutubePost.objects.filter(category__contains="memes and vines").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryReviews(request):
    infoImage = ImagePost.objects.filter(category__contains="music and series review")
    imageCount = ImagePost.objects.filter(category__contains="music and series review").count()
    infoVideo = VideoPost.objects.filter(category__contains="music and series review")
    videoCount = VideoPost.objects.filter(category__contains="music and series review").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="music and series review")
    youtubeCount = YoutubePost.objects.filter(category__contains="music and series review").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryPolitics(request):
    infoImage = ImagePost.objects.filter(category__contains="politics")
    imageCount = ImagePost.objects.filter(category__contains="politics").count()
    infoVideo = VideoPost.objects.filter(category__contains="politics")
    videoCount = VideoPost.objects.filter(category__contains="politics").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="politics")
    youtubeCount = YoutubePost.objects.filter(category__contains="politics").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categorySports(request):
    infoImage = ImagePost.objects.filter(category__contains="sports")
    imageCount = ImagePost.objects.filter(category__contains="sports").count()
    infoVideo = VideoPost.objects.filter(category__contains="sports")
    videoCount = VideoPost.objects.filter(category__contains="sports").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="sports")
    youtubeCount = YoutubePost.objects.filter(category__contains="sports").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryTechnology(request):
    infoImage = ImagePost.objects.filter(category__contains="technology")
    imageCount = ImagePost.objects.filter(category__contains="technology").count()
    infoVideo = VideoPost.objects.filter(category__contains="technology")
    videoCount = VideoPost.objects.filter(category__contains="technology").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="technology")
    youtubeCount = YoutubePost.objects.filter(category__contains="technology").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryYouths(request):
    infoImage = ImagePost.objects.filter(category__contains="youths corner")
    imageCount = ImagePost.objects.filter(category__contains="youths corner").count()
    infoVideo = VideoPost.objects.filter(category__contains="youths corner")
    videoCount = VideoPost.objects.filter(category__contains="youths corner").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="youths corner")
    youtubeCount = YoutubePost.objects.filter(category__contains="youths corner").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
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


# Gallery Function
def gallery(request):
    image = ImagePost.objects.order_by('?')
    context = {
        'image': image,
    }
    return render(request, 'appBlogd/gallery.html', context)

# Contact Function
