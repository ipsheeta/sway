from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=200)
    graph_snippet = models.TextField(blank=True)
    point = models.CharField(max_length=50, blank=True)
    image = models.FileField(upload_to="file/image/",blank=True)
    mp3 = models.FileField(upload_to="file/audio/",blank=True)
    ogg = models.FileField(upload_to="file/audio/",blank=True)

    def __unicode__(self):
        return self.title