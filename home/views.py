from django.shortcuts import get_object_or_404, render
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
