from django.shortcuts import render
from .models import Announce, Member

# Create your views here.
def index_page(request):
    return render(request, 'blog/index.html')

def about_page(request):
    return render(request, 'blog/about.html')

def aboutkor_page(request):
    return render(request, 'blog/about_kor.html')

def research_page(request):
    return render(request, 'blog/research.html')

def member_page(request):
    directors = Member.objects.filter(type='D')
    return render(request, 'blog/member_direct.html', {'directors': directors})

def member_senior(request):
    seniors = Member.objects.filter(type='S')
    return render(request, 'blog/member_senior.html', {'seniors': seniors})

def member_res(request):
    researchers = Member.objects.filter(type='R')
    return render(request, 'blog/member_res.html', {'researchers': researchers})

def notice_page(request):
    announces = Announce.objects.all().order_by('published_date')
    return render(request, 'blog/notice.html', {'announces': announces})

def notice_each(request, id=None):
    announce = Announce.objects.get(pk=id)
    return render(request, 'blog/notice_each.html', {'announce': announce})

def contact_page(request):
    return render(request, 'blog/contact.html')
