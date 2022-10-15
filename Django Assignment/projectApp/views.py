from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import GeeksForm
from .models import GeeksModel11
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.
def index(request):
    return HttpResponse('This is new App')

# Create your views here.
#7
# def home_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "home.html", context)

#8.1
# Create your views here.
# def home_view(request):
#     # logic of view will be implemented here
#     print(request.GET)
#     return render(request, "home.html")

#8.2
# Create your views here.
# def home_view(request):
#     # logic of view will be implemented here
#     print(request.POST)
#     return render(request, "home.html")

# 9
def home_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)

#10
# importing formset_factory
from django.forms import formset_factory
  
def formset_view(request):
    context ={}
  
    # creating a formset
    GeeksFormSet = formset_factory(GeeksForm, extra=5)
    formset = GeeksFormSet(request.POST or None)
    
    #print formset data is it's valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)


    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)

#11 - ModelFormset Factory
from .models import GeeksModel11
from django.forms import modelformset_factory
def formset_model(request):
    context={}

    GeeksModelFormSet = modelformset_factory(GeeksModel11, fields=['title', 'description'], extra=5)
    modelformset = GeeksModelFormSet(request.POST or None)

    #print formset data is it's valid
    if modelformset.is_valid():
        for form in modelformset:
            print(form.cleaned_data)
    
    # Add the formset to context dictionary
    context['formset']= modelformset
    return render(request, "home.html", context)

#12 - Templates
def geeks_view(request):
    context = {'data':"Full Stack Cloud Dev is the best!",
                'list': [1,2,3,4,5,6,7,8,9,10]}
    return render(request, 'geeks_view.html', context)


#13. 
import datetime
 
# create a function
def geeks_templ_view1(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def list_view(request):
    # dictionary for initial data with field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel11.objects.all()
         
    return render(request, "list_view.html", context)

from django.views.generic.list import ListView
class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel11

#14.
def create_view(request):
    # dictionary for initial data with field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)

# relative import of forms
from .models import GeeksModel11
 
# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel11.objects.get(id = id)
         
    return render(request, "detail_view.html", context)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel11, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel11, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)