from django.shortcuts import get_object_or_404, render
from django.views.generic import View   # needed to make class based views
from .models import Tag, Startup
from .forms import TagForm, StartupForm, NewsLinkForm
from .utils import ObjectCreateMixin


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class StartupCreate(ObjectCreateMixin, View):
    form_class= StartupForm
    template_name = 'organizer/startup_form.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name='organizer/newslink_form.html'


def tag_list(request):
    return render(request,'organizer/tag_list.html',{'tag_list':Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request,'organizer/tag_detail.html',{'tag':tag})


def startup_list(request):
    return render(request,'organizer/startup_list.html',{'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request,'organizer/startup_detail.html', {'startup':startup})


    '''This function is now rendered uselass as we have created the class above it
    def tag_create(request):
        if request.method =='POST':
            # bind data to the form
            form = TagForm(request.POST)
            # if the data is valid:
            if form.is_valid():
                # create a new object from teh data
                new_tag = form.save()
                #show webpage for new object
                return redirect(new_tag)
        else:   # else if no data or invalid data
            form = TagForm()
            # SHOW BOUND Form
        return render(request, 'organizer/tag_form.html', {'form':form })
    '''