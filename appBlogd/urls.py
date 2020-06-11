from django.urls import path
from . import views

app_name = 'appBlogd'

urlpatterns = [
    # Index Page Url
    path('', views.index, name='index'),

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
]