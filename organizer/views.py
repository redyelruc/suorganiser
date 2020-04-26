from django.shortcuts import get_object_or_404, render, redirect,reverse
from django.views.generic import View   # needed to make class based views
from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm
from .utils import ObjectCreateMixin, ObjectUpdateMixin


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name =('organizer/tag_form_update.html')

class StartupCreate(ObjectCreateMixin, View):
    form_class= StartupForm
    template_name = 'organizer/startup_form.html'

class StartupUpdate(ObjectUpdateMixin,View):
    form_class = StartupForm
    model = Startup
    template_name = 'organizer/startup_form_update.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name='organizer/newslink_form.html'


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name =('organizer/newslink_form_update.html')


    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink,pk=pk)
        context = {'form': self.form_class(instance=newslink), 'newslink': newslink,}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404 (NewsLink, pk=pk)
        bound_form = self.form_class(request.POST, instance = newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {'form':bound_form, 'newslink' : newslink}
            return render(request, self.template_name,context)



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