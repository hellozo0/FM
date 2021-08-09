from django.shortcuts import render, get_object_or_404, redirect
from .models import Community #Community에서의 데이터를 가져오기 위해 --> community.html에서 사용될 듯
from .forms import PostForm, SearchForm
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

# 아래 함수들 다 수정해야함. 목적에 맞게 id를 받는다거나...등등
def search(request):
    form = SearchForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            배 = request.POST.get("배", None)
    return render(request, 'search.html',{"form":form})

def detail(request):
    return render(request, 'detail.html') 

def community(request):
    q = Community.objects.order_by('-id')
    q_list = Community.objects.all().order_by('-id')
    paginator = Paginator(q_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'community.html',{'quiz':q, 'posts':posts})

def map(request):
    return render(request, 'map.html')

def developers(request):
    return render(request, 'developers.html')

#여기서 새로운 함수를 만들면 --> 새로운 페이지를 만들었다는 거니까 --> urls.py에 지정해주기 
def new(request):
    return render(request, 'new.html')
    
def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post = form.save()
            return redirect('community')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, community_id):
    post = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('writef', community_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def writef(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'writef.html', {'community':community_detail})

def postdelete(request, community_id):
    post = get_object_or_404(Community, pk=community_id)
    post.delete()
    return redirect('community')

def post_search(request):
    blogs = Community.objects.all().order_by('-id')

    q = request.POST.get('q', "") 
    title_q = Q(title__icontains = q)
    body_q = Q(body__icontains = q)
    
    if q:
        blogs = blogs.filter(title_q | body_q)
        return render(request, 'post_search.html', {'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'post_search.html')
   