from django.contrib import admin
from .models import ImagePost, VideoPost, YoutubePost, ImagePostComment, VideoPostComment, YoutubePostComment

# Register your models here.
admin.site.register(ImagePost)
admin.site.register(VideoPost)
admin.site.register(YoutubePost)
admin.site.register(ImagePostComment)
admin.site.register(VideoPostComment)
admin.site.register(YoutubePostComment)
