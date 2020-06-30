from django.urls import path
from . import views

app_name = 'appBlogd'

handler404 = 'appBlogd.views.error_404'

urlpatterns = [
    # Index Page Url
    path('', views.loader, name='loader'),

    path('index', views.index, name='index'),

    # Category Urls
    path('category-business', views.categoryBusiness, name='catBusiness'),
    path('category-cars', views.categoryCar, name='catCars'),
    path('category-celebrity', views.categoryCelebrity, name='catCelebrity'),
    path('category-history', views.categoryHistory, name='catHistory'),
    path('category-lifestyle', views.categoryLifestyle, name='catLifestyle'),
    path('category-matatu_culture', views.categoryMatatu, name='catMatatu'),
    path('category-memes_vines', views.categoryMemes, name='catMemes'),
    path('category-movies_series_review', views.categoryReviews, name='catReviews'),
    path('category-politics', views.categoryPolitics, name='catPolitics'),
    path('category-sports', views.categorySports, name='catSports'),
    path('category-technology', views.categoryTechnology, name='catTechnology'),
    path('category-youths_corner', views.categoryYouths, name='catYouths'),

    # View Image Post Url
    path('view-image-post/code:<int:view_id>', views.viewImage_post, name='viewImage_post'),

    # View Image Post Url
    path('view-video-post/code:<int:view_id>', views.viewVideo_post, name='viewVideo_post'),

    # View Youtube Post Url
    path('view-youtube-post/code:<int:view_id>', views.viewYoutube_post, name='viewYoutube_post'),

    # Gallery Url
    path('gallery', views.gallery, name='gallery'),

    # Contact Url
    path('contact_us', views.contact, name='contact'),

    # Text Post Admin Url
    path('text_post-admin', views.text_post_admin, name='text_post_admin'),

    # Video Post Admin Url
    path('video_post-admin', views.video_post_admin, name='video_post_admin'),

    # Youtube Post Admin Url
    path('youtube_post-admin', views.youtube_post_admin, name='youtube_post_admin'),

    # Text Post Form Url
    path('new_text_post', views.textPostForm, name='text_post_form'),

    # Video Post Form Url
    path('upload_video_post', views.videoPostForm, name='video_post_form'),

    # Youtube Post Form Url
    path('post_youtube_video', views.youtubePostForm, name='youtube_post_form'),

    # Delete Text Post Url
    path('delete_text_post/code:<int:post_id>', views.text_post_delete, name='delete_text_post'),

    # Delete Video Post Url
    path('delete_video_post/code:<int:post_id>', views.video_post_delete, name='delete_video_post'),

    # Delete Youtube Post Url
    path('delete_youtube_post/code:<int:post_id>', views.youtube_post_delete, name='delete_youtube_post'),

    # Update Text Post Url
    path('update_text_post/code:<int:post_id>', views.update_text_post, name='update_text_post'),

    # Update Video Post Url
    path('update_video_post/code:<int:post_id>', views.update_video_post, name='update_video_post'),

    # Update Youtube Post Url
    path('update_youtube_post/code:<int:post_id>', views.update_youtube_post, name='update_youtube_post'),

    # Contact Admin
    path('contact|subscribers', views.contact_admin, name='contact_admin'),

    # Delete Subscriber Url
    path('delete_subscriber/code:<int:post_id>', views.subscriber_delete, name='delete_subscriber'),

    # Administrators Url
    path('administrators_table', views.admins, name='admins_table'),

    # Admin Login
    path('login', views.admin_login, name='admin_login'),

    # Register Admin
    path('admin_register', views.admin_register, name='admin_register'),

    # Update Admin
    path('update_admin/code:<int:post_id>', views.update_admin, name='update_admin'),

    # Delete Admin
    path('delete_admin/code:<int:post_id>', views.delete_admin, name='delete_admin'),

    # Logout Admin
    path('logout', views.logout_admin, name='logout_admin'),

    # Index Admin
    path('index-admin', views.index_admin, name='index_admin'),

    # Search
    path('results/$', views.search, name="search"),
]