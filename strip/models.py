from django.db import models


class FrameMedia(models.Model):
    upload_user = models.ForeignKey('User')
    media_path = models.CharField(max_length=255)


class Frame(models.Model):
    user = models.ForeignKey('User')
    caption = models.TextField(null=True, blank=True)
    media = models.ForeignKey('FrameMedia')


class Strip(models.Model):
    title = models.CharField(max_length=255)


class StripFrame(models.Model):
    frame = models.ForeignKey(Frame)
    strip = models.ForeignKey(Strip)
