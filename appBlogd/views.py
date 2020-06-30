from django.shortcuts import render, get_object_or_404, redirect
from .models import ImagePost, VideoPost, YoutubePost, Contact
from .forms import ContactForm, TextPostForm, YoutubePostForm, VideoPostForm, FormUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
# Text Posts
def loader(request):
    return render(request, 'appBlogd/loader.html')


def index(request):
    infoImage = ImagePost.objects.order_by('?')
    infoVideo = VideoPost.objects.filter(upload_category__contains="video")
    infoAudio = VideoPost.objects.filter(upload_category__contains="audio")
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
        'posts': posts,
        'infoVideo': infoVideo,
        'infoAudio': infoAudio,
        'infoYoutube': infoYoutube,

    }
    return render(request, 'appBlogd/index.html', context)


# Category Viewing Functions
def categoryBusiness(request):
    infoImage = ImagePost.objects.filter(category__contains="business")
    imageCount = ImagePost.objects.filter(category__contains="business").count()
    infoVideo = VideoPost.objects.filter(category__contains="business", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="business", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="business", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="business", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="business")
    youtubeCount = YoutubePost.objects.filter(category__contains="business").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryCar(request):
    infoImage = ImagePost.objects.filter(category__contains="cars")
    imageCount = ImagePost.objects.filter(category__contains="cars").count()
    infoVideo = VideoPost.objects.filter(category__contains="cars", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="cars", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="cars", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="cars", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="cars")
    youtubeCount = YoutubePost.objects.filter(category__contains="cars").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryCelebrity(request):
    infoImage = ImagePost.objects.filter(category__contains="celebrity")
    imageCount = ImagePost.objects.filter(category__contains="celebrity").count()
    infoVideo = VideoPost.objects.filter(category__contains="celebrity", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="celebrity", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="celebrity", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="celebrity", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="celebrity")
    youtubeCount = YoutubePost.objects.filter(category__contains="celebrity").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryHistory(request):
    infoImage = ImagePost.objects.filter(category__contains="history")
    imageCount = ImagePost.objects.filter(category__contains="history").count()
    infoVideo = VideoPost.objects.filter(category__contains="history", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="history", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="history", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="history", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="history")
    youtubeCount = YoutubePost.objects.filter(category__contains="history").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryLifestyle(request):
    infoImage = ImagePost.objects.filter(category__contains="lifestyle")
    imageCount = ImagePost.objects.filter(category__contains="lifestyle").count()
    infoVideo = VideoPost.objects.filter(category__contains="lifestyle", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="lifestyle", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="lifestyle", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="lifestyle", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="lifestyle")
    youtubeCount = YoutubePost.objects.filter(category__contains="lifestyle").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryMatatu(request):
    infoImage = ImagePost.objects.filter(category__contains="matatu culture")
    imageCount = ImagePost.objects.filter(category__contains="matatu culture").count()
    infoVideo = VideoPost.objects.filter(category__contains="matatu culture", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="matatu culture", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="matatu culture", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="matatu culture", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="matatu culture")
    youtubeCount = YoutubePost.objects.filter(category__contains="matatu culture").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryMemes(request):
    infoImage = ImagePost.objects.filter(category__contains="memes and vines")
    imageCount = ImagePost.objects.filter(category__contains="memes and vines").count()
    infoVideo = VideoPost.objects.filter(category__contains="memes and vines", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="memes and vines", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="memes and vines", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="memes and vines", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="memes and vines")
    youtubeCount = YoutubePost.objects.filter(category__contains="memes and vines").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryReviews(request):
    infoImage = ImagePost.objects.filter(category__contains="music and series review")
    imageCount = ImagePost.objects.filter(category__contains="music and series review").count()
    infoVideo = VideoPost.objects.filter(category__contains="music and series review", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="music and series review", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="music and series review", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="music and series review", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="music and series review")
    youtubeCount = YoutubePost.objects.filter(category__contains="music and series review").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryPolitics(request):
    infoImage = ImagePost.objects.filter(category__contains="politics")
    imageCount = ImagePost.objects.filter(category__contains="politics").count()
    infoVideo = VideoPost.objects.filter(category__contains="politics", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="politics", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="politics", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="politics", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="politics")
    youtubeCount = YoutubePost.objects.filter(category__contains="politics").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categorySports(request):
    infoImage = ImagePost.objects.filter(category__contains="sports")
    imageCount = ImagePost.objects.filter(category__contains="sports").count()
    infoVideo = VideoPost.objects.filter(category__contains="sports", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="sports", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="sports", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="sports", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="sports")
    youtubeCount = YoutubePost.objects.filter(category__contains="sports").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryTechnology(request):
    infoImage = ImagePost.objects.filter(category__contains="technology")
    imageCount = ImagePost.objects.filter(category__contains="technology").count()
    infoVideo = VideoPost.objects.filter(category__contains="technology", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="technology", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="technology", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="technology", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="technology")
    youtubeCount = YoutubePost.objects.filter(category__contains="technology").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
        'infoYoutube': infoYoutube,
        'youtubeCount': youtubeCount,
    }
    return render(request, 'appBlogd/category.html', context)


def categoryYouths(request):
    infoImage = ImagePost.objects.filter(category__contains="youths corner")
    imageCount = ImagePost.objects.filter(category__contains="youths corner").count()
    infoVideo = VideoPost.objects.filter(category__contains="youths corner", upload_category__contains="video")
    videoCount = VideoPost.objects.filter(category__contains="youths corner", upload_category__contains="video").count()
    infoAudio = VideoPost.objects.filter(category__contains="youths corner", upload_category__contains="audio")
    audioCount = VideoPost.objects.filter(category__contains="youths corner", upload_category__contains="audio").count()
    infoYoutube = YoutubePost.objects.filter(category__contains="youths corner")
    youtubeCount = YoutubePost.objects.filter(category__contains="youths corner").count()
    context = {
        'infoImage': infoImage,
        'imageCount': imageCount,
        'infoVideo': infoVideo,
        'videoCount': videoCount,
        'infoAudio': infoAudio,
        'audioCount': audioCount,
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
    paginator = Paginator(image, 30)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
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


@login_required(login_url='appBlogd:admin_login')
# Text Post Admin
def text_post_admin(request):
    text_post = ImagePost.objects.order_by('id')
    context = {
        'text_post': text_post,
    }
    return render(request, 'appBlogd/admin/text_post_admin.html', context)


@login_required(login_url='appBlogd:admin_login')
# Video Post Admin
def video_post_admin(request):
    post = VideoPost.objects.order_by('id')
    context = {
        'post': post,
    }
    return render(request, 'appBlogd/admin/video_post_admin.html', context)


@login_required(login_url='appBlogd:admin_login')
# Youtube Post Admin
def youtube_post_admin(request):
    post = YoutubePost.objects.order_by('id')
    context = {
        'post': post,
    }
    return render(request, 'appBlogd/admin/youtube_post_admin.html', context)


@login_required(login_url='appBlogd:admin_login')
# Text Posting Function
def textPostForm(request):
    form = TextPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('appBlogd:text_post_admin')
    return render(request, 'appBlogd/admin/text_post_form.html', {'form': form})


@login_required(login_url='appBlogd:admin_login')
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


@login_required(login_url='appBlogd:admin_login')
# Youtube Posting Function
def youtubePostForm(request):
    form = YoutubePostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appBlogd:youtube_post_admin')
    return render(request, 'appBlogd/admin/youtube_post_form.html', {'form': form})


@login_required(login_url='appBlogd:admin_login')
# Delete Text Post
def text_post_delete(request, post_id):
    post = get_object_or_404(ImagePost, pk=post_id)
    post.delete()
    return redirect('appBlogd:text_post_admin')


@login_required(login_url='appBlogd:admin_login')
# Delete Video Post
def video_post_delete(request, post_id):
    post = get_object_or_404(VideoPost, pk=post_id)
    post.delete()
    return redirect('appBlogd:video_post_admin')


@login_required(login_url='appBlogd:admin_login')
# Delete Youtube Post
def youtube_post_delete(request, post_id):
    post = get_object_or_404(YoutubePost, pk=post_id)
    post.delete()
    return redirect('appBlogd:youtube_post_admin')


@login_required(login_url='appBlogd:admin_login')
# Update Text Post
def update_text_post(request, post_id):
    post = get_object_or_404(ImagePost, pk=post_id)
    form = TextPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:text_post_admin')
    return render(request, 'appBlogd/admin/text_post_form.html', {'form': form})


@login_required(login_url='appBlogd:admin_login')
# Update Video Post
def update_video_post(request, post_id):
    post = get_object_or_404(VideoPost, pk=post_id)
    form = VideoPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:video_post_admin')
    return render(request, 'appBlogd/admin/video_post_form.html', {'form': form})


@login_required(login_url='appBlogd:admin_login')
# Update Text Post
def update_youtube_post(request, post_id):
    post = get_object_or_404(YoutubePost, pk=post_id)
    form = YoutubePostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:youtube_post_admin')
    return render(request, 'appBlogd/admin/youtube_post_form.html', {'form': form})


@login_required(login_url='appBlogd:admin_login')
# Contact Admin
def contact_admin(request):
    post = Contact.objects.order_by('id')
    context = {
        'post': post,
    }
    return render(request, 'appBlogd/admin/contact_admin.html', context)


@login_required(login_url='appBlogd:admin_login')
# Delete Subscriber Post
def subscriber_delete(request, post_id):
    post = get_object_or_404(Contact, pk=post_id)
    post.delete()
    return redirect('appBlogd:contact_admin')


# Administrators Function
def admins(request):
    result = User.objects.order_by('id')
    context = {
        'result': result,
    }
    return render(request, 'appBlogd/admin/admins.html', context)


#Login Admin
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('appBlogd:index_admin')
        else:
            message = {'message': 'Invalid Credentials'}
            return render(request, 'appBlogd/admin/admin_login.html', message)
    return render(request, 'appBlogd/admin/admin_login.html')



# Register Admin
def admin_register(request):
    form = FormUser(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        regist = form.save(commit=False)
        regist.set_password(password)
        regist.save()
        authenticate(username=username, password=password)
        return redirect('appBlogd:admins_table')
    return render(request, 'appBlogd/admin/admin_register.html', {'form': form})


# Update Text Post
def update_admin(request, post_id):
    post = get_object_or_404(User, pk=post_id)
    form = FormUser(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('appBlogd:admins_table')
    context = {
        'form': form,
        'update': 'update',
    }
    return render(request, 'appBlogd/admin/admin_register.html', context)


@login_required(login_url='appBlogd:admin_login')
# Delete Youtube Post
def delete_admin(request, post_id):
    post = get_object_or_404(User, pk=post_id)
    post.delete()
    return redirect('appBlogd:admins_table')


# Logout Admin
def logout_admin(request):
    logout(request)
    return redirect('appBlogd:index')


@login_required(login_url='appBlogd:admin_login')
# Index Admin
def index_admin(request):
    return render(request, 'appBlogd/admin/index_admin.html')


def search(request):
    template = 'appBlogd/index.html'
    query = request.GET.get('q')
    resultImage = ImagePost.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    resultVideo = VideoPost.objects.filter(Q(title__icontains=query) | Q(category__icontains=query), upload_category__contains="video")
    resultAudio = VideoPost.objects.filter(Q(title__icontains=query) | Q(category__icontains=query), upload_category__contains="audio")
    resultYoutube = YoutubePost.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    message = "🔍 This is all we could find ................. 👇🏾"
    context = {
        'posts': resultImage,
        'infoVideo': resultVideo,
        'infoAudio': resultAudio,
        'infoYoutube': resultYoutube,
        'message': message,
    }
    return render(request, template, context)


def error_404(request, exception):
    data = {}
    return render(request, 'appBlogd/404.html', data)