from itertools import count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from home.models import News, Comment
from .forms import NewsForm
from django.db.models import Count

# Create your views here.
def home_view(request):
    articles = News.objects.annotate(comment_count=Count('comment')).order_by('-date')[:9]
    context = {"articles": articles}
    return render(request, "index.html", context)
    
def about(request):
    return(render(request,'about.html'))

def contact(request):
    return(render(request,'contactus.html'))

def allnews(request):
    article=News.objects.annotate(comment_count=Count('comment')).all()
    return(render(request,'all_news.html',{'articles':article}))



def detailnews(request, id):
    news = get_object_or_404(News, pk = id)
    comment = news.comment_set.all()
    comment_count = comment.all().count()
    # detail = {'detail': news}
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment_post = form.save(commit=False)
            comment_post.post = news
            comment_post.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('detailnews', id = id)
        


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewsForm()



    context = {
        'news': news,
        'form': form,
        'comments': comment,
        'total_comment': comment_count
        
    }
    # return render(request, "form.html", {"form": form})
    return render(request, 'detail_news.html', context)






def newhome(request):
    return(render(request,'newhomepage.html'))


def newdetail(request):
    return(render(request,'newdetailpage.html'))