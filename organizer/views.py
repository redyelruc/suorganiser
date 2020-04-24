from django.shortcuts import get_object_or_404, render
from .models import Tag, Startup
from django.shortcuts import get_object_or_404, render

from .models import Tag, Startup


def tag_list(request):
    '''tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list':tag_list}
    output = template.render(context)
    return HttpResponse(output)'''
    #all this code has been replaced by

    return render(request,'organizer/tag_list.html',{'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    #template =  loader.get_template('organizer/tag_detail.html')
    #context = {'tag': tag}
    #return HttpResponse(template.render(context))
    return render(request,'organizer/tag_detail.html',{'tag':tag})

def startup_list(request):
    return render(request,'organizer/startup_list.html',{'startup_list': Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request,'organizer/startup_detail.html', {'startup':startup})