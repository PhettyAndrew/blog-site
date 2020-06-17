from django.shortcuts import render, get_object_or_404, redirect
from .models import ImagePost, VideoPost, YoutubePost, Contact
from .forms import ContactForm, TextPostForm, YoutubePostForm, VideoPostForm
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
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        success = {
            'success': 'Registration Successful!!',
            'form': form,
        }
        return render(request, 'appBlogd/contact.html', success)
    return render(request, 'appBlogd/contact.html', {'form': form})


# Text Post Admin
def text_post_admin(request):
    text_post = ImagePost.objects.order_by('id')
    context = {
        'text_post': text_post,
    }
    return render(request, 'appBlogd/admin/text_post_admin.html', context)


# Video Post Admin
def video_post_admin(request):
    post = VideoPost.objects.order_by('id')
    context = {
        'post': post,
    }
    return render(request, 'appBlogd/admin/video_post_admin.html', context)


# Youtube Post Admin
def youtube_post_admin(request):
    post = YoutubePost.objects.order_by('id')
    context = {
        'post': post,
    }
    return render(request, 'appBlogd/admin/youtube_post_admin.html', context)


# Text Posting Function
def textPostForm(request):
    form = TextPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('appBlogd:text_post_admin')
    return render(request, 'appBlogd/admin/text_post_form.html', {'form': form})


# Video Posting Function
def videoPostForm(request):
    if request.method == 'POST':
        form = VideoPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('appBlogd:video_post_admin')
    else:
        form = VideoPostForm()
    return render(request, 'appBlogd/admin/video_post_form.html', {'form': form})


# Youtube Posting Function
def youtubePostForm(request):
    form = YoutubePostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appBlogd:youtube_post_admin')
    return render(request, 'appBlogd/admin/youtube_post_form.html', {'form': form})


# Delete Text Post
def text_post_delete(request, post_id):
    post = get_object_or_404(ImagePost, pk=post_id)
    post.delete()
    return redirect('appBlogd:text_post_admin')


# Delete Video Post
def video_post_delete(request, post_id):
    post = get_object_or_404(VideoPost, pk=post_id)
    post.delete()
    return redirect('appBlogd:video_post_admin')


# Delete Youtube Post
def youtube_post_delete(request, post_id):
    post = get_object_or_404(YoutubePost, pk=post_id)
    post.delete()
    return redirect('appBlogd:youtube_post_admin')


# Update Text Post
def update_text_post(request, post_id):
    post = get_object_or_404(ImagePost, pk=post_id)
    form = TextPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:text_post_admin')
    return render(request, 'appBlogd/admin/text_post_form.html', {'form': form})


# Update Video Post
def update_video_post(request, post_id):
    post = get_object_or_404(VideoPost, pk=post_id)
    form = VideoPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:video_post_admin')
    return render(request, 'appBlogd/admin/video_post_form.html', {'form': form})


# Update Text Post
def update_youtube_post(request, post_id):
    post = get_object_or_404(YoutubePost, pk=post_id)
    form = YoutubePostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:youtube_post_admin')
    return render(request, 'appBlogd/admin/youtube_post_form.html', {'form': form})


# Contact Admin
def contact_admin(request):
    post = Contact.objects.order_by('id')
    context = {
        'post': post,
    }
    return render(request, 'appBlogd/admin/contact_admin.html', context)