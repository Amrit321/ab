from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from home.forms import NewsForm
from home.models import News

# Create your views here.
def home_view(request):
    latest_article=News.objects.order_by('-date')[:9]
    return render(request, "index.html",{'articles':latest_article})

def about(request):
    return(render(request,'about.html'))

def contact(request):
    return(render(request,'contactus.html'))

def allnews(request):
    article=News.objects.all()
    return(render(request,'all_news.html',{'articles':article}))

def detailnews(request, id):
    context = get_object_or_404(News, pk = id)
    detail = {'detail': context}
    return render(request, 'detail_news.html', detail)


def newsform(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect(reverse('news_form'))
        


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewsForm()

    return render(request, "form.html", {"form": form})