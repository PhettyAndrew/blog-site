from django.contrib import admin
from .models import ImagePost, VideoPost, YoutubePost, Contact

# Register your models here.
admin.site.register(ImagePost)
admin.site.register(VideoPost)
admin.site.register(YoutubePost)
admin.site.register(Contact)
