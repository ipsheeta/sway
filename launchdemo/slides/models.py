from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=200)
    graph_snippet = models.TextField(blank=True)
    point = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.title