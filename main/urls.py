from django.urls import path
from . import views
from register import views as v
from .views import NewsFeed, NewsDetail


app_name = 'blog'

urlpatterns = [
    # post views
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("qu-est-ce-qu-un-pangolin/", views.about, name="about"),
    path("about/", views.about, name="about"),
    path("threats/", views.threat, name="threats"),
    path("conservation/", views.conservation, name="conservation"),
    path("gabon/", views.gabon, name="gabon"),
    path("faq/", views.faq, name="faq"),
    path("actions/", views.action, name="actions"),
    path("pcp/", views.pcp, name="pcp"),
    path("funds/", views.fund, name="funds"),
    path("wpd/", views.wpd, name="wpd"),
    path('news/', NewsFeed.as_view(), name='news_feed'),
#   path("news/", views.news, name="news"),
    path("help/", views.help, name="help"),
    path("resources/", views.resource, name="resources"),
    path("meet/", views.meet, name="meet"),
    path("partners/", views.partner, name="partner"),

    path("create_news/", views.create_news, name="create_news"),

    path('<slug:slug>/', NewsDetail.as_view(), name='news_detail'),

    

]
