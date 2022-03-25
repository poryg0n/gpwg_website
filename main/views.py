from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import CreateNewNews
from django.utils.text import slugify
from .models import (
        Post,
        Main,
        MainItem,
        About,
        AboutItem,
        Threat,
        ThreatItem,
        Conservation,
        ConservationItem,
        Gabon,
        GabonItem,
        FAQ,
        FAQItem,
        Action,
        ActionItem,
        PCP,
        PCPItem,
        Fund,
        FundItem,
        WPD,
        WPDItem,
        New,
        NewItem,
        Help,
        HelpItem,
        Resource,
        ResourceItem,
        Meet,
        MeetItem,
        Partner,
        PartnerItem
        )


# Create your views here.
def home(request):
    posts = Main.objects.get(id=1)
    print(posts.name)
#   return HttpResponse("<h1>Gabon Pangolin Working Group</h1>")
    return render(request,"main/home.html", {"posts": posts})

def about(request):
    posts = About.objects.get(id=1)
#   about_posts = About.objects.get(id=1)
#   posts = about_posts.aboutitem_set.all()
    print(posts.header)
    return render(request, "main/about.html", {"posts":posts})

def threat(request):
    posts = Threat.objects.get(id=1)
    print(posts)
    return render(request, "main/threat.html", {"posts":posts})

def conservation(request):
    posts = Conservation.objects.get(id=1)
    print(posts)
    return render(request, "main/conservation.html", {"posts":posts})

def gabon(request):
    posts = Gabon.objects.get(id=1)
    print(posts)
    return render(request, "main/gabon.html", {"posts":posts})

def faq(request):
    posts = FAQ.objects.get(id=1)
    print(posts)
    return render(request, "main/faq.html", {"posts":posts})

def action(request):
    posts = Action.objects.get(id=1)
    print(posts)
    return render(request, "main/action.html", {"posts":posts})

def pcp(request):
    posts = PCP.objects.get(id=1)
    print(posts)
    return render(request, "main/pcp.html", {"posts":posts})

def fund(request):
    posts = Fund.objects.get(id=1)
    print(posts)
    return render(request, "main/fund.html", {"posts":posts})

def wpd(request):
    posts = WPD.objects.get(id=1)
    print(posts)
    return render(request, "main/wpd.html", {"posts":posts})

#def news(request):
#    news_posts = New.objects.get(id=1)
#    posts = news_posts.newitem_set.all()
#    print(posts)
#    return render(request, "main/news.html", {"posts":posts})

def help(request):
    posts = Help.objects.get(id=1)
    print(posts)
    return render(request, "main/help.html", {"posts":posts})

def resource(request):
    posts = Resource.objects.get(id=1)
    print(posts)
    return render(request, "main/resource.html", {"posts":posts})

def meet(request):
    posts = Meet.objects.get(id=1)
    print(posts)
    return render(request, "main/meet.html", {"posts":posts})

def partner(request):
    posts = Partner.objects.get(id=1)
    print(posts)
    return render(request, "main/partners.html", {"posts":posts})

def create_news(request):
    context={}

    new = New.objects.get(id=1)
    if request.method == "POST":
        form = CreateNewNews(request.POST, request.FILES, initial={'new': new})

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            print(new)
            instance.slug = slugify(instance.title)
            instance.save()

            context['form'] = form
            return render(request, "main/news_feed.html", context)
    else:
        form = CreateNewNews()
    return render(request, "main/create_news.html", {"form":form})


class NewsFeed(ListView):
#   model = Post
    model = NewItem
    context_object_name = 'posts'
    template_name = 'main/news_feed.html'


class NewsDetail(DetailView):
#   model = Post
    model = NewItem
    context_object_name = 'post'
    template_name = 'main/news_detail.html'
