from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import View   # needed to make class based views
from .models import Tag, Startup
from .forms import TagForm, StartupForm


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

class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self,request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template_name, {'form':bound_form})

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
def startup_list(request):
    return render(request,'organizer/startup_list.html',{'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request,'organizer/startup_detail.html', {'startup':startup})

class StartupCreate(View):
    form_class= StartupForm
    template_name = 'organizer/startup_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template_name,{'form': bound_form})



