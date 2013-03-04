from django.shortcuts import render_to_response
from models import Slide
from django.template import RequestContext

def SlideShow(request):
    temp = Slide.objects.all()
    return render_to_response('launchdemo/demo.html',
                              {'slide_list':temp}, context_instance = RequestContext(request))
