from django.shortcuts import render, get_object_or_404, redirect
from .models import Community  #Community에서의 데이터를 가져오기 위해 --> community.html에서 사용될 듯
from .forms import PostForm

def home(request):
    return render(request, 'home.html')



# 아래 함수들 다 수정해야함. 목적에 맞게 id를 받는다거나...등등
def search(request):
    return render(request, 'search.html')

def detail(request):
    return render(request, 'detail.html') 

def community(request):
    communities = Community.objects.all().order_by('-id')
    return render(request, 'community.html', {"communities":communities})

def map(request):
    return render(request, 'map.html')

#여기서 새로운 함수를 만들면 --> 새로운 페이지를 만들었다는 거니까 --> urls.py에 지정해주기 
def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
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
            return redirect('write', community_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def write(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'write.html', {'community':community_detail})

def postdelete(request, community_id):
    post = get_object_or_404(Community, pk=community_id)
    post.delete()
    return redirect('community')