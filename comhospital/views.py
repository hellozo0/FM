from django.shortcuts import render, get_object_or_404, redirect
from .models import ComHospital #Community에서의 데이터를 가져오기 위해 --> community.html에서 사용될 듯
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.
def comhospital(request):
    q = ComHospital.objects.order_by('-id')
    q_list = ComHospital.objects.all().order_by('-id')
    paginator = Paginator(q_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'comhospital.html',{'quiz':q, 'posts':posts})

def news(request):
    return render(request, 'news.html')

def postcreates(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('comhospital')
    else:
        form = PostForm()
        return render(request, 'news.html', {'form':form})

def edits(request):
    return render(request, 'edits.html')

def postupdates(request, comhospital_id):
    post = get_object_or_404(ComHospital, pk=comhospital_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('writes', comhospital_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edits.html', {'form':form})

def postdeletes(request, comhospital_id):
    post = get_object_or_404(ComHospital, pk=comhospital_id)
    post.delete()
    return redirect('comhospital')

def writes(request, comhospital_id):
    comhospital_detail = get_object_or_404(ComHospital, pk=comhospital_id)
    return render(request, 'writes.html', {'comhospital':comhospital_detail})