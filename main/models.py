from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)
#   slug = models.SlugField(max_length=250,
#                           unique=True)
#   author = models.ForeignKey(User,
#                              on_delete=models.CASCADE,
#                              related_name='main_posts')
#   body = models.TextField()
#   publish = models.DateTimeField(default=timezone.now)
#   image = models.ImageField(blank=True, upload_to='images')

#   class Meta:
#       ordering = ('publish',)

    def __str__(self):
        return self.name

#   def get_absolute_url(self):
#       return reverse('main:slug', args=[self.slug])
#       return redirect('main/<slug:slug>', args=[self.slug])

class MainItem(models.Model):
    posts = models.ForeignKey(Main, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='main_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class AboutItem(models.Model):
    posts = models.ForeignKey(About, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True, blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='about_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Threat(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ThreatItem(models.Model):
    posts = models.ForeignKey(Threat, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='threat_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title

class Conservation(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ConservationItem(models.Model):
    posts = models.ForeignKey(Conservation, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='conservation_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Gabon(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class GabonItem(models.Model):
    posts = models.ForeignKey(Gabon, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='gabon_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class FAQItem(models.Model):
    posts = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='faq_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Action(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ActionItem(models.Model):
    posts = models.ForeignKey(Action, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='ouraction_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class PCP(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class PCPItem(models.Model):
    posts = models.ForeignKey(PCP, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='pcp_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Fund(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class FundItem(models.Model):
    posts = models.ForeignKey(Fund, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='fund_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class WPD(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class WPDItem(models.Model):
    posts = models.ForeignKey(WPD, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='wpd_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class New(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class NewItem(models.Model):
    posts = models.ForeignKey(New, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='new_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:news_detail', args=[self.slug])



class Help(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class HelpItem(models.Model):
    posts = models.ForeignKey(Help, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='help_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Resource(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ResourceItem(models.Model):
    posts = models.ForeignKey(Resource, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='resource_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Meet(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class MeetItem(models.Model):
    posts = models.ForeignKey(Meet, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='meet_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class PartnerItem(models.Model):
    posts = models.ForeignKey(Partner, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
#   text = models.CharField(max_length=300)
#   complete = models.BooleanField()

    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='partner_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    header = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='news_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:news_detail', args=[self.slug])



