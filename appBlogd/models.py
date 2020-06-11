from django.db import models

# Create your models here.
# Category Tuple
category = (
    ('Unknown', 'unknown'),
    ('Lifestyle', 'lifestyle'),
    ('Business', 'business'),
    ('Cars', 'cars'),
    ('Celebrity', 'celebrity'),
    ('History', 'history'),
    ('Matatu Culture', 'matatu culture'),
    ('Memes and Vines', 'memes and vines'),
    ('Music and Series Review', 'music and series review'),
    ('Politics', 'politics'),
    ('Sports', 'sports'),
    ('Technology', 'technology'),
    ('Youths Corner', 'youths corner'),
)


# Post Table
class ImagePost(models.Model):
    image = models.ImageField()
    category = models.CharField(choices=category, default='unknown', max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    story = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Video Table
class VideoPost(models.Model):
    video = models.FileField()
    category = models.CharField(choices=category, default='unknown', max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    story = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Youtube Videos Table
class YoutubePost(models.Model):
    url = models.CharField(max_length=20)
    category = models.CharField(choices=category, default='unknown', max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    story = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Post Comment Table
class ImagePostComment(models.Model):
    post = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


# Post Comment Table
class VideoPostComment(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


# Post Comment Table
class YoutubePostComment(models.Model):
    post = models.ForeignKey(YoutubePost, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name
