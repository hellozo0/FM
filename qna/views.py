from django.shortcuts import render, get_object_or_404, redirect
from .models import Qna #Community에서의 데이터를 가져오기 위해 --> community.html에서 사용될 듯
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.
def qna(request):
    q = Qna.objects.order_by('-id')
    q_list = Qna.objects.all().order_by('-id')
    paginator = Paginator(q_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'qna.html',{'quiz':q, 'posts':posts})

def newt(request):
    return render(request, 'newt.html')

def postcreatet(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('qna')
    else:
        form = PostForm()
        return render(request, 'newt.html', {'form':form})

def editt(request):
    return render(request, 'editt.html')

def postupdatet(request, qna_id):
    post = get_object_or_404(Qna, pk=qna_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('writet', qna_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'editt.html', {'form':form})

def postdeletet(request, qna_id):
    post = get_object_or_404(Qna, pk=qna_id)
    post.delete()
    return redirect('qna')

def writet(request, qna_id):
    qna_detail = get_object_or_404(Qna, pk=qna_id)
    return render(request, 'writet.html', {'qna':qna_detail})